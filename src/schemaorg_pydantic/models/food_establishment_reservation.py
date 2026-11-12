from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import DateTime, Integer, Is, Ref, Time
from .reservation import Reservation

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

DateTime_Time = Union[DateTime, Time]
if TYPE_CHECKING:
    QuantitativeValue_Integer_Ref = Union[QuantitativeValue, Integer, Ref]
else:
    QuantitativeValue_Integer_Ref = Union[Is["QuantitativeValue"], Integer, Ref]


class FoodEstablishmentReservation(Reservation):
    """A reservation to dine at a food-related business."""
    schema_type: ClassVar[str] = "FoodEstablishmentReservation"
    end_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="endTime", serialization_alias="endTime")
    party_size: QuantitativeValue_Integer_Ref | list[QuantitativeValue_Integer_Ref] | None = Field(default=None, validation_alias="partySize", serialization_alias="partySize")
    start_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="startTime", serialization_alias="startTime")
