from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class BikeStore(Store):
    """A bike store."""
    schema_type: ClassVar[str] = "BikeStore"
