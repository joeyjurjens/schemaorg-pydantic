from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .structured_value import StructuredValue
from .drive_wheel_configuration_value import DriveWheelConfigurationValue
from .steering_position_value import SteeringPositionValue

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

DriveWheelConfigurationValue_SteeringPositionValue_Text = Union[DriveWheelConfigurationValue, SteeringPositionValue, Text]
if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]


class EngineSpecification(StructuredValue):
    """Information about the engine of the vehicle. A vehicle can have multiple engines represented by multiple engine specification entities."""
    schema_type: ClassVar[str] = "EngineSpecification"
    engine_displacement: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="engineDisplacement", serialization_alias="engineDisplacement")
    engine_power: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="enginePower", serialization_alias="enginePower")
    engine_type: DriveWheelConfigurationValue_SteeringPositionValue_Text | list[DriveWheelConfigurationValue_SteeringPositionValue_Text] | None = Field(default=None, validation_alias="engineType", serialization_alias="engineType")
    fuel_type: DriveWheelConfigurationValue_SteeringPositionValue_Text | list[DriveWheelConfigurationValue_SteeringPositionValue_Text] | None = Field(default=None, validation_alias="fuelType", serialization_alias="fuelType")
    torque: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None)
