import argparse
import hashlib
import json
import re
import shutil
import sys
import urllib.request
from pathlib import Path

from .generator import Generator
from .vocabulary import Vocabulary

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
PACKAGE = ROOT / "src" / "schemaorg_pydantic"
PIN = SCRIPTS / "pin.json"

CHANGED = 10
LISTING = "https://api.github.com/repos/schemaorg/schemaorg/contents/data/releases"
FILE = (
    "https://raw.githubusercontent.com/schemaorg/schemaorg/main/data/releases/"
    "{version}/schemaorg-current-https.jsonld"
)
VERSION = re.compile(r"^\d+(\.\d+)*$")


class ReleaseSource:
    def fetch(self, url):
        request = urllib.request.Request(url, headers={"User-Agent": "schemaorg-pydantic"})
        with urllib.request.urlopen(request, timeout=60) as response:
            return response.read()

    @staticmethod
    def version_key(version):
        return tuple(int(part) for part in version.split("."))

    @classmethod
    def newest(cls, names):
        versions = [name for name in names if VERSION.match(name)]
        return max(versions, key=cls.version_key) if versions else None

    def latest(self):
        listing = json.loads(self.fetch(LISTING))
        return self.newest(entry["name"] for entry in listing if entry["type"] == "dir")

    def download(self, version):
        data = self.fetch(FILE.format(version=version))
        return data, hashlib.sha256(data).hexdigest()


class Updater:
    def __init__(self, source=None):
        self.source = source or ReleaseSource()

    def pinned(self):
        return json.loads(PIN.read_text())

    def generate(self, data, release):
        generator = Generator(
            Vocabulary(json.loads(data)["@graph"]),
            json.loads((SCRIPTS / "range_overrides.json").read_text()),
        )
        files = generator.files(release)
        shutil.rmtree(PACKAGE / "models", ignore_errors=True)
        for path, source in files.items():
            target = PACKAGE / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(source)
        return generator.stats()

    def write_pin(self, version, sha):
        PIN.write_text(json.dumps({"release": version, "sha256": sha}, indent=2) + "\n")

    def run(self, latest):
        pinned = self.pinned()
        version = self.source.latest() if latest else pinned["release"]
        data, sha = self.source.download(version)
        if not latest and sha != pinned["sha256"]:
            raise SystemExit(f"release {version} is not the pinned file: {sha}")
        stats = self.generate(data, version)
        self.write_pin(version, sha)
        changed = (version, sha) != (pinned["release"], pinned["sha256"])
        print(json.dumps({"release": version, "changed": changed, **stats}))
        return CHANGED if changed else 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--latest", action="store_true")
    sys.exit(Updater().run(parser.parse_args().latest))


if __name__ == "__main__":
    main()
