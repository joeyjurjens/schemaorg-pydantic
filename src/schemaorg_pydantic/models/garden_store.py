from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class GardenStore(Store):
    """A garden store."""
    schema_type: ClassVar[str] = "GardenStore"
