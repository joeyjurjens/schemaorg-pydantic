from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class ShoeStore(Store):
    """A shoe store."""
    schema_type: ClassVar[str] = "ShoeStore"
