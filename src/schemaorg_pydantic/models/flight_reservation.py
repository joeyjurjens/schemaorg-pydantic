from __future__ import annotations

from typing import ClassVar, Union

from pydantic import Field

from ..base import Text
from .reservation import Reservation
from .drive_wheel_configuration_value import DriveWheelConfigurationValue
from .steering_position_value import SteeringPositionValue

DriveWheelConfigurationValue_SteeringPositionValue_Text = Union[DriveWheelConfigurationValue, SteeringPositionValue, Text]

class FlightReservation(Reservation):
    """A reservation for air travel."""
    schema_type: ClassVar[str] = "FlightReservation"
    boarding_group: Text | list[Text] | None = Field(default=None, validation_alias="boardingGroup", serialization_alias="boardingGroup")
    passenger_priority_status: DriveWheelConfigurationValue_SteeringPositionValue_Text | list[DriveWheelConfigurationValue_SteeringPositionValue_Text] | None = Field(default=None, validation_alias="passengerPriorityStatus", serialization_alias="passengerPriorityStatus")
    passenger_sequence_number: Text | list[Text] | None = Field(default=None, validation_alias="passengerSequenceNumber", serialization_alias="passengerSequenceNumber")
    security_screening: Text | list[Text] | None = Field(default=None, validation_alias="securityScreening", serialization_alias="securityScreening")
