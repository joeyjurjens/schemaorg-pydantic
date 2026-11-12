import importlib
import sys
from typing import Any


class LazyExports:
    def __init__(self, package: str, modules: dict[str, str]) -> None:
        self.package = package
        self.modules = modules

    def get(self, name: str) -> Any:
        if name not in self.modules:
            raise AttributeError(f"module {self.package!r} has no attribute {name!r}")
        module = importlib.import_module(f"{self.package}.models.{self.modules[name]}")
        value = getattr(module, name)
        setattr(sys.modules[self.package], name, value)
        return value

    def names(self) -> list[str]:
        return sorted(set(vars(sys.modules[self.package])) | set(self.modules))
