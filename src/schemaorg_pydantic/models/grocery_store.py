from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class GroceryStore(Store):
    """A grocery store."""
    schema_type: ClassVar[str] = "GroceryStore"
