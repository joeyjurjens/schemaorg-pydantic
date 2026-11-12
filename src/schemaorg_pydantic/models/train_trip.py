from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .trip import Trip

if TYPE_CHECKING:
    from .train_station import TrainStation

if TYPE_CHECKING:
    TrainStation_Ref = Union[TrainStation, Ref]
else:
    TrainStation_Ref = Union[Is["TrainStation"], Ref]


class TrainTrip(Trip):
    """A trip on a commercial train line."""
    schema_type: ClassVar[str] = "TrainTrip"
    arrival_platform: Text | list[Text] | None = Field(default=None, validation_alias="arrivalPlatform", serialization_alias="arrivalPlatform")
    arrival_station: TrainStation_Ref | list[TrainStation_Ref] | None = Field(default=None, validation_alias="arrivalStation", serialization_alias="arrivalStation")
    departure_platform: Text | list[Text] | None = Field(default=None, validation_alias="departurePlatform", serialization_alias="departurePlatform")
    departure_station: TrainStation_Ref | list[TrainStation_Ref] | None = Field(default=None, validation_alias="departureStation", serialization_alias="departureStation")
    train_name: Text | list[Text] | None = Field(default=None, validation_alias="trainName", serialization_alias="trainName")
    train_number: Text | list[Text] | None = Field(default=None, validation_alias="trainNumber", serialization_alias="trainNumber")
