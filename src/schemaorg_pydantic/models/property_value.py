from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Number, Ref, Text
from .structured_value import StructuredValue
from .body_measurement_type_enumeration import BodyMeasurementTypeEnumeration
from .drive_wheel_configuration_value import DriveWheelConfigurationValue
from .measurement_method_enum import MeasurementMethodEnum
from .steering_position_value import SteeringPositionValue
from .wearable_measurement_type_enumeration import WearableMeasurementTypeEnumeration

if TYPE_CHECKING:
    from .defined_term import DefinedTerm
    from .enumeration import Enumeration
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    Rac3092bf = Union[BodyMeasurementTypeEnumeration, DefinedTerm, DriveWheelConfigurationValue, Enumeration, "PropertyValue", QuantitativeValue, SteeringPositionValue, StructuredValue, WearableMeasurementTypeEnumeration, Text, Ref]
else:
    Rac3092bf = Union[BodyMeasurementTypeEnumeration, Is["DefinedTerm"], DriveWheelConfigurationValue, Is["Enumeration"], Is["PropertyValue"], Is["QuantitativeValue"], SteeringPositionValue, Is["StructuredValue"], WearableMeasurementTypeEnumeration, Text, Ref]

if TYPE_CHECKING:
    DefinedTerm_MeasurementMethodEnum_Text_Ref = Union[DefinedTerm, MeasurementMethodEnum, Text, Ref]
else:
    DefinedTerm_MeasurementMethodEnum_Text_Ref = Union[Is["DefinedTerm"], MeasurementMethodEnum, Text, Ref]

if TYPE_CHECKING:
    R3f96830d = Union[DriveWheelConfigurationValue, SteeringPositionValue, StructuredValue, Boolean, Number, Text, Ref]
else:
    R3f96830d = Union[DriveWheelConfigurationValue, SteeringPositionValue, Is["StructuredValue"], Boolean, Number, Text, Ref]


class PropertyValue(StructuredValue):
    """A property-value pair, e.g. representing a feature of a product or place. Use the 'name' property for the name of the property. If there is an additional human-readable version of the value, put that into the 'description' property."""
    schema_type: ClassVar[str] = "PropertyValue"
    max_value: Number | list[Number] | None = Field(default=None, validation_alias="maxValue", serialization_alias="maxValue")
    measurement_method: DefinedTerm_MeasurementMethodEnum_Text_Ref | list[DefinedTerm_MeasurementMethodEnum_Text_Ref] | None = Field(default=None, validation_alias="measurementMethod", serialization_alias="measurementMethod")
    measurement_technique: DefinedTerm_MeasurementMethodEnum_Text_Ref | list[DefinedTerm_MeasurementMethodEnum_Text_Ref] | None = Field(default=None, validation_alias="measurementTechnique", serialization_alias="measurementTechnique")
    min_value: Number | list[Number] | None = Field(default=None, validation_alias="minValue", serialization_alias="minValue")
    property_id: Text | list[Text] | None = Field(default=None, validation_alias="propertyID", serialization_alias="propertyID")
    unit_code: Text | list[Text] | None = Field(default=None, validation_alias="unitCode", serialization_alias="unitCode")
    unit_text: Text | list[Text] | None = Field(default=None, validation_alias="unitText", serialization_alias="unitText")
    value: R3f96830d | list[R3f96830d] | None = Field(default=None)
    value_group: Text | list[Text] | None = Field(default=None, validation_alias="valueGroup", serialization_alias="valueGroup")
    value_reference: Rac3092bf | list[Rac3092bf] | None = Field(default=None, validation_alias="valueReference", serialization_alias="valueReference")
