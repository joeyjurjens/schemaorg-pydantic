from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class FurnitureStore(Store):
    """A furniture store."""
    schema_type: ClassVar[str] = "FurnitureStore"
