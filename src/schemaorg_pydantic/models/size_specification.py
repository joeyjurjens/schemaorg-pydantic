from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .qualitative_value import QualitativeValue
from .gender_type import GenderType
from .size_system_enumeration import SizeSystemEnumeration
from .wearable_size_group_enumeration import WearableSizeGroupEnumeration
from .wearable_size_system_enumeration import WearableSizeSystemEnumeration

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

GenderType_Text = Union[GenderType, Text]
if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]

SizeSystemEnumeration_WearableSizeSystemEnumeration_Text = Union[SizeSystemEnumeration, WearableSizeSystemEnumeration, Text]
WearableSizeGroupEnumeration_Text = Union[WearableSizeGroupEnumeration, Text]

class SizeSpecification(QualitativeValue):
    """Size related properties of a product, typically a size code ([[name]]) and optionally a [[sizeSystem]], [[sizeGroup]], and product measurements ([[hasMeasurement]]). In addition, the intended audience can be defined through [[suggestedAge]], [[suggestedGender]], and suggested body measurements ([[suggestedMeasurement]])."""
    schema_type: ClassVar[str] = "SizeSpecification"
    has_measurement: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="hasMeasurement", serialization_alias="hasMeasurement")
    size_group: WearableSizeGroupEnumeration_Text | list[WearableSizeGroupEnumeration_Text] | None = Field(default=None, validation_alias="sizeGroup", serialization_alias="sizeGroup")
    size_system: SizeSystemEnumeration_WearableSizeSystemEnumeration_Text | list[SizeSystemEnumeration_WearableSizeSystemEnumeration_Text] | None = Field(default=None, validation_alias="sizeSystem", serialization_alias="sizeSystem")
    suggested_age: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="suggestedAge", serialization_alias="suggestedAge")
    suggested_gender: GenderType_Text | list[GenderType_Text] | None = Field(default=None, validation_alias="suggestedGender", serialization_alias="suggestedGender")
    suggested_measurement: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="suggestedMeasurement", serialization_alias="suggestedMeasurement")
