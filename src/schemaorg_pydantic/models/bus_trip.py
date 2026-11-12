from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .trip import Trip

if TYPE_CHECKING:
    from .bus_station import BusStation
    from .bus_stop import BusStop

if TYPE_CHECKING:
    BusStation_BusStop_Ref = Union[BusStation, BusStop, Ref]
else:
    BusStation_BusStop_Ref = Union[Is["BusStation"], Is["BusStop"], Ref]


class BusTrip(Trip):
    """A trip on a commercial bus line."""
    schema_type: ClassVar[str] = "BusTrip"
    arrival_bus_stop: BusStation_BusStop_Ref | list[BusStation_BusStop_Ref] | None = Field(default=None, validation_alias="arrivalBusStop", serialization_alias="arrivalBusStop")
    bus_name: Text | list[Text] | None = Field(default=None, validation_alias="busName", serialization_alias="busName")
    bus_number: Text | list[Text] | None = Field(default=None, validation_alias="busNumber", serialization_alias="busNumber")
    departure_bus_stop: BusStation_BusStop_Ref | list[BusStation_BusStop_Ref] | None = Field(default=None, validation_alias="departureBusStop", serialization_alias="departureBusStop")
