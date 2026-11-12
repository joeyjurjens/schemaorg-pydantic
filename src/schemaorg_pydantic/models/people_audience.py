from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Number, Ref, Text
from .audience import Audience
from .gender_type import GenderType

if TYPE_CHECKING:
    from .medical_condition import MedicalCondition
    from .quantitative_value import QuantitativeValue

GenderType_Text = Union[GenderType, Text]
if TYPE_CHECKING:
    MedicalCondition_Ref = Union[MedicalCondition, Ref]
else:
    MedicalCondition_Ref = Union[Is["MedicalCondition"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]


class PeopleAudience(Audience):
    """A set of characteristics belonging to people, e.g. who compose an item's target audience."""
    schema_type: ClassVar[str] = "PeopleAudience"
    health_condition: MedicalCondition_Ref | list[MedicalCondition_Ref] | None = Field(default=None, validation_alias="healthCondition", serialization_alias="healthCondition")
    required_gender: Text | list[Text] | None = Field(default=None, validation_alias="requiredGender", serialization_alias="requiredGender")
    required_max_age: Integer | list[Integer] | None = Field(default=None, validation_alias="requiredMaxAge", serialization_alias="requiredMaxAge")
    required_min_age: Integer | list[Integer] | None = Field(default=None, validation_alias="requiredMinAge", serialization_alias="requiredMinAge")
    suggested_age: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="suggestedAge", serialization_alias="suggestedAge")
    suggested_gender: GenderType_Text | list[GenderType_Text] | None = Field(default=None, validation_alias="suggestedGender", serialization_alias="suggestedGender")
    suggested_max_age: Number | list[Number] | None = Field(default=None, validation_alias="suggestedMaxAge", serialization_alias="suggestedMaxAge")
    suggested_measurement: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="suggestedMeasurement", serialization_alias="suggestedMeasurement")
    suggested_min_age: Number | list[Number] | None = Field(default=None, validation_alias="suggestedMinAge", serialization_alias="suggestedMinAge")
