from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class JewelryStore(Store):
    """A jewelry store."""
    schema_type: ClassVar[str] = "JewelryStore"
