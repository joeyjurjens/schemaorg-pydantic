from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .enumeration import Enumeration
from .body_measurement_type_enumeration import BodyMeasurementTypeEnumeration
from .drive_wheel_configuration_value import DriveWheelConfigurationValue
from .steering_position_value import SteeringPositionValue
from .wearable_measurement_type_enumeration import WearableMeasurementTypeEnumeration

if TYPE_CHECKING:
    from .defined_term import DefinedTerm
    from .property_value import PropertyValue
    from .quantitative_value import QuantitativeValue
    from .structured_value import StructuredValue

if TYPE_CHECKING:
    Rac3092bf = Union[BodyMeasurementTypeEnumeration, DefinedTerm, DriveWheelConfigurationValue, Enumeration, PropertyValue, QuantitativeValue, SteeringPositionValue, StructuredValue, WearableMeasurementTypeEnumeration, Text, Ref]
else:
    Rac3092bf = Union[BodyMeasurementTypeEnumeration, Is["DefinedTerm"], DriveWheelConfigurationValue, Is["Enumeration"], Is["PropertyValue"], Is["QuantitativeValue"], SteeringPositionValue, Is["StructuredValue"], WearableMeasurementTypeEnumeration, Text, Ref]

DriveWheelConfigurationValue_SteeringPositionValue = Union[DriveWheelConfigurationValue, SteeringPositionValue]
if TYPE_CHECKING:
    PropertyValue_Ref = Union[PropertyValue, Ref]
else:
    PropertyValue_Ref = Union[Is["PropertyValue"], Ref]


class QualitativeValue(Enumeration):
    """A predefined value for a product characteristic, e.g. the power cord plug type 'US' or the garment sizes 'S', 'M', 'L', and 'XL'."""
    schema_type: ClassVar[str] = "QualitativeValue"
    additional_property: PropertyValue_Ref | list[PropertyValue_Ref] | None = Field(default=None, validation_alias="additionalProperty", serialization_alias="additionalProperty")
    equal: DriveWheelConfigurationValue_SteeringPositionValue | list[DriveWheelConfigurationValue_SteeringPositionValue] | None = Field(default=None)
    greater: DriveWheelConfigurationValue_SteeringPositionValue | list[DriveWheelConfigurationValue_SteeringPositionValue] | None = Field(default=None)
    greater_or_equal: DriveWheelConfigurationValue_SteeringPositionValue | list[DriveWheelConfigurationValue_SteeringPositionValue] | None = Field(default=None, validation_alias="greaterOrEqual", serialization_alias="greaterOrEqual")
    lesser: DriveWheelConfigurationValue_SteeringPositionValue | list[DriveWheelConfigurationValue_SteeringPositionValue] | None = Field(default=None)
    lesser_or_equal: DriveWheelConfigurationValue_SteeringPositionValue | list[DriveWheelConfigurationValue_SteeringPositionValue] | None = Field(default=None, validation_alias="lesserOrEqual", serialization_alias="lesserOrEqual")
    non_equal: DriveWheelConfigurationValue_SteeringPositionValue | list[DriveWheelConfigurationValue_SteeringPositionValue] | None = Field(default=None, validation_alias="nonEqual", serialization_alias="nonEqual")
    value_reference: Rac3092bf | list[Rac3092bf] | None = Field(default=None, validation_alias="valueReference", serialization_alias="valueReference")
