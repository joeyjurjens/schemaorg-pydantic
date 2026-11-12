from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import DateTime, Is, Ref, Text
from .trip import Trip
from .boarding_policy_type import BoardingPolicyType

if TYPE_CHECKING:
    from .airport import Airport
    from .organization import Organization
    from .person import Person
    from .vehicle import Vehicle

if TYPE_CHECKING:
    Airport_Ref = Union[Airport, Ref]
else:
    Airport_Ref = Union[Is["Airport"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Vehicle_Text_Ref = Union[Vehicle, Text, Ref]
else:
    Vehicle_Text_Ref = Union[Is["Vehicle"], Text, Ref]


class Flight(Trip):
    """An airline flight."""
    schema_type: ClassVar[str] = "Flight"
    aircraft: Vehicle_Text_Ref | list[Vehicle_Text_Ref] | None = Field(default=None)
    arrival_airport: Airport_Ref | list[Airport_Ref] | None = Field(default=None, validation_alias="arrivalAirport", serialization_alias="arrivalAirport")
    arrival_gate: Text | list[Text] | None = Field(default=None, validation_alias="arrivalGate", serialization_alias="arrivalGate")
    arrival_terminal: Text | list[Text] | None = Field(default=None, validation_alias="arrivalTerminal", serialization_alias="arrivalTerminal")
    boarding_policy: BoardingPolicyType | list[BoardingPolicyType] | None = Field(default=None, validation_alias="boardingPolicy", serialization_alias="boardingPolicy")
    departure_airport: Airport_Ref | list[Airport_Ref] | None = Field(default=None, validation_alias="departureAirport", serialization_alias="departureAirport")
    departure_gate: Text | list[Text] | None = Field(default=None, validation_alias="departureGate", serialization_alias="departureGate")
    departure_terminal: Text | list[Text] | None = Field(default=None, validation_alias="departureTerminal", serialization_alias="departureTerminal")
    estimated_flight_duration: Text | list[Text] | None = Field(default=None, validation_alias="estimatedFlightDuration", serialization_alias="estimatedFlightDuration")
    flight_distance: Text | list[Text] | None = Field(default=None, validation_alias="flightDistance", serialization_alias="flightDistance")
    flight_number: Text | list[Text] | None = Field(default=None, validation_alias="flightNumber", serialization_alias="flightNumber")
    meal_service: Text | list[Text] | None = Field(default=None, validation_alias="mealService", serialization_alias="mealService")
    seller: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    web_checkin_time: DateTime | list[DateTime] | None = Field(default=None, validation_alias="webCheckinTime", serialization_alias="webCheckinTime")
