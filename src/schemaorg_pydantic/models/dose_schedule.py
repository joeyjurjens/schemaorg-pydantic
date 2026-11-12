from __future__ import annotations

from typing import ClassVar, Union

from pydantic import Field

from ..base import Number, Text
from .medical_intangible import MedicalIntangible
from .drive_wheel_configuration_value import DriveWheelConfigurationValue
from .steering_position_value import SteeringPositionValue

DriveWheelConfigurationValue_SteeringPositionValue_Number = Union[DriveWheelConfigurationValue, SteeringPositionValue, Number]

class DoseSchedule(MedicalIntangible):
    """A specific dosing schedule for a drug or supplement."""
    schema_type: ClassVar[str] = "DoseSchedule"
    dose_unit: Text | list[Text] | None = Field(default=None, validation_alias="doseUnit", serialization_alias="doseUnit")
    dose_value: DriveWheelConfigurationValue_SteeringPositionValue_Number | list[DriveWheelConfigurationValue_SteeringPositionValue_Number] | None = Field(default=None, validation_alias="doseValue", serialization_alias="doseValue")
    frequency: Text | list[Text] | None = Field(default=None)
    target_population: Text | list[Text] | None = Field(default=None, validation_alias="targetPopulation", serialization_alias="targetPopulation")
