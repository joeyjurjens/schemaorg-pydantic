from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import DateTime, Integer, Is, Ref, Text, Time
from .reservation import Reservation
from .drive_wheel_configuration_value import DriveWheelConfigurationValue
from .steering_position_value import SteeringPositionValue

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

DateTime_Time = Union[DateTime, Time]
DriveWheelConfigurationValue_SteeringPositionValue_Text = Union[DriveWheelConfigurationValue, SteeringPositionValue, Text]
if TYPE_CHECKING:
    QuantitativeValue_Integer_Ref = Union[QuantitativeValue, Integer, Ref]
else:
    QuantitativeValue_Integer_Ref = Union[Is["QuantitativeValue"], Integer, Ref]


class LodgingReservation(Reservation):
    """A reservation for lodging at a hotel, motel, inn, etc."""
    schema_type: ClassVar[str] = "LodgingReservation"
    checkin_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="checkinTime", serialization_alias="checkinTime")
    checkout_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="checkoutTime", serialization_alias="checkoutTime")
    lodging_unit_description: Text | list[Text] | None = Field(default=None, validation_alias="lodgingUnitDescription", serialization_alias="lodgingUnitDescription")
    lodging_unit_type: DriveWheelConfigurationValue_SteeringPositionValue_Text | list[DriveWheelConfigurationValue_SteeringPositionValue_Text] | None = Field(default=None, validation_alias="lodgingUnitType", serialization_alias="lodgingUnitType")
    num_adults: QuantitativeValue_Integer_Ref | list[QuantitativeValue_Integer_Ref] | None = Field(default=None, validation_alias="numAdults", serialization_alias="numAdults")
    num_children: QuantitativeValue_Integer_Ref | list[QuantitativeValue_Integer_Ref] | None = Field(default=None, validation_alias="numChildren", serialization_alias="numChildren")
