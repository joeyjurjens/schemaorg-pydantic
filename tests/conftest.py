import json
from pathlib import Path

import pytest

from scripts.update import ReleaseSource
from scripts.vocabulary import Vocabulary

ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def vocabulary():
    pin = json.loads((ROOT / "scripts" / "pin.json").read_text())
    cache = ROOT / ".cache" / f"schemaorg-{pin['release']}.jsonld"
    if not cache.exists():
        try:
            data, sha = ReleaseSource().download(pin["release"])
        except OSError:
            pytest.skip("the pinned schema.org release cannot be downloaded")
        assert sha == pin["sha256"]
        cache.parent.mkdir(exist_ok=True)
        cache.write_bytes(data)
    return Vocabulary(json.loads(cache.read_text())["@graph"])
