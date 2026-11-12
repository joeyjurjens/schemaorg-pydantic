from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class ElectronicsStore(Store):
    """An electronics store."""
    schema_type: ClassVar[str] = "ElectronicsStore"
