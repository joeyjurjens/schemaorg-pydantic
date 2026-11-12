from __future__ import annotations

from typing import ClassVar, Union

from pydantic import Field

from ..base import Text
from .intangible import Intangible
from .drive_wheel_configuration_value import DriveWheelConfigurationValue
from .steering_position_value import SteeringPositionValue

DriveWheelConfigurationValue_SteeringPositionValue_Text = Union[DriveWheelConfigurationValue, SteeringPositionValue, Text]

class Seat(Intangible):
    """Used to describe a seat, such as a reserved seat in an event reservation."""
    schema_type: ClassVar[str] = "Seat"
    seat_number: Text | list[Text] | None = Field(default=None, validation_alias="seatNumber", serialization_alias="seatNumber")
    seat_row: Text | list[Text] | None = Field(default=None, validation_alias="seatRow", serialization_alias="seatRow")
    seat_section: Text | list[Text] | None = Field(default=None, validation_alias="seatSection", serialization_alias="seatSection")
    seating_type: DriveWheelConfigurationValue_SteeringPositionValue_Text | list[DriveWheelConfigurationValue_SteeringPositionValue_Text] | None = Field(default=None, validation_alias="seatingType", serialization_alias="seatingType")
