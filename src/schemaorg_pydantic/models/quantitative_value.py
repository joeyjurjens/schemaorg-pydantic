from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Number, Ref, Text
from .structured_value import StructuredValue
from .body_measurement_type_enumeration import BodyMeasurementTypeEnumeration
from .drive_wheel_configuration_value import DriveWheelConfigurationValue
from .steering_position_value import SteeringPositionValue
from .wearable_measurement_type_enumeration import WearableMeasurementTypeEnumeration

if TYPE_CHECKING:
    from .defined_term import DefinedTerm
    from .enumeration import Enumeration
    from .property_value import PropertyValue

if TYPE_CHECKING:
    Rac3092bf = Union[BodyMeasurementTypeEnumeration, DefinedTerm, DriveWheelConfigurationValue, Enumeration, PropertyValue, "QuantitativeValue", SteeringPositionValue, StructuredValue, WearableMeasurementTypeEnumeration, Text, Ref]
else:
    Rac3092bf = Union[BodyMeasurementTypeEnumeration, Is["DefinedTerm"], DriveWheelConfigurationValue, Is["Enumeration"], Is["PropertyValue"], Is["QuantitativeValue"], SteeringPositionValue, Is["StructuredValue"], WearableMeasurementTypeEnumeration, Text, Ref]

if TYPE_CHECKING:
    R3f96830d = Union[DriveWheelConfigurationValue, SteeringPositionValue, StructuredValue, Boolean, Number, Text, Ref]
else:
    R3f96830d = Union[DriveWheelConfigurationValue, SteeringPositionValue, Is["StructuredValue"], Boolean, Number, Text, Ref]

if TYPE_CHECKING:
    PropertyValue_Ref = Union[PropertyValue, Ref]
else:
    PropertyValue_Ref = Union[Is["PropertyValue"], Ref]


class QuantitativeValue(StructuredValue):
    """A point value or interval for product characteristics and other purposes."""
    schema_type: ClassVar[str] = "QuantitativeValue"
    additional_property: PropertyValue_Ref | list[PropertyValue_Ref] | None = Field(default=None, validation_alias="additionalProperty", serialization_alias="additionalProperty")
    max_value: Number | list[Number] | None = Field(default=None, validation_alias="maxValue", serialization_alias="maxValue")
    min_value: Number | list[Number] | None = Field(default=None, validation_alias="minValue", serialization_alias="minValue")
    unit_code: Text | list[Text] | None = Field(default=None, validation_alias="unitCode", serialization_alias="unitCode")
    unit_text: Text | list[Text] | None = Field(default=None, validation_alias="unitText", serialization_alias="unitText")
    value: R3f96830d | list[R3f96830d] | None = Field(default=None)
    value_reference: Rac3092bf | list[Rac3092bf] | None = Field(default=None, validation_alias="valueReference", serialization_alias="valueReference")
