from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .place import Place

if TYPE_CHECKING:
    from .floor_plan import FloorPlan

if TYPE_CHECKING:
    FloorPlan_Ref = Union[FloorPlan, Ref]
else:
    FloorPlan_Ref = Union[Is["FloorPlan"], Ref]


class Residence(Place):
    """The place where a person lives."""
    schema_type: ClassVar[str] = "Residence"
    accommodation_floor_plan: FloorPlan_Ref | list[FloorPlan_Ref] | None = Field(default=None, validation_alias="accommodationFloorPlan", serialization_alias="accommodationFloorPlan")
    floor_level: Text | list[Text] | None = Field(default=None, validation_alias="floorLevel", serialization_alias="floorLevel")
