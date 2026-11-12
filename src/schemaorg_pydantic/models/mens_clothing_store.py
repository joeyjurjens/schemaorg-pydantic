from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class MensClothingStore(Store):
    """A men's clothing store."""
    schema_type: ClassVar[str] = "MensClothingStore"
