from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import DateTime, Is, Ref
from .reservation import Reservation

if TYPE_CHECKING:
    from .place import Place

if TYPE_CHECKING:
    Place_Ref = Union[Place, Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]


class RentalCarReservation(Reservation):
    """A reservation for a rental car."""
    schema_type: ClassVar[str] = "RentalCarReservation"
    dropoff_location: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="dropoffLocation", serialization_alias="dropoffLocation")
    dropoff_time: DateTime | list[DateTime] | None = Field(default=None, validation_alias="dropoffTime", serialization_alias="dropoffTime")
    pickup_location: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="pickupLocation", serialization_alias="pickupLocation")
    pickup_time: DateTime | list[DateTime] | None = Field(default=None, validation_alias="pickupTime", serialization_alias="pickupTime")
