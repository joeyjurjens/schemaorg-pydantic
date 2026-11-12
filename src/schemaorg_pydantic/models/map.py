from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work import CreativeWork
from .map_category_type import MapCategoryType


class Map(CreativeWork):
    """A map."""
    schema_type: ClassVar[str] = "Map"
    map_type: MapCategoryType | list[MapCategoryType] | None = Field(default=None, validation_alias="mapType", serialization_alias="mapType")
