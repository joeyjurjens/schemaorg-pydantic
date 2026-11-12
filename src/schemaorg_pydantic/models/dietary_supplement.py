from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Ref, Text
from .product import Product
from .substance import Substance

if TYPE_CHECKING:
    from .recommended_dose_schedule import RecommendedDoseSchedule

if TYPE_CHECKING:
    RecommendedDoseSchedule_Ref = Union[RecommendedDoseSchedule, Ref]
else:
    RecommendedDoseSchedule_Ref = Union[Is["RecommendedDoseSchedule"], Ref]


class DietarySupplement(Product, Substance):
    """A product taken by mouth that contains a dietary ingredient intended to supplement the diet. Dietary ingredients may include vitamins, minerals, herbs or other botanicals, amino acids, and substances such as enzymes, organ tissues, glandulars and metabolites."""
    schema_type: ClassVar[str] = "DietarySupplement"
    is_proprietary: Boolean | list[Boolean] | None = Field(default=None, validation_alias="isProprietary", serialization_alias="isProprietary")
    mechanism_of_action: Text | list[Text] | None = Field(default=None, validation_alias="mechanismOfAction", serialization_alias="mechanismOfAction")
    non_proprietary_name: Text | list[Text] | None = Field(default=None, validation_alias="nonProprietaryName", serialization_alias="nonProprietaryName")
    proprietary_name: Text | list[Text] | None = Field(default=None, validation_alias="proprietaryName", serialization_alias="proprietaryName")
    recommended_intake: RecommendedDoseSchedule_Ref | list[RecommendedDoseSchedule_Ref] | None = Field(default=None, validation_alias="recommendedIntake", serialization_alias="recommendedIntake")
    safety_consideration: Text | list[Text] | None = Field(default=None, validation_alias="safetyConsideration", serialization_alias="safetyConsideration")
    target_population: Text | list[Text] | None = Field(default=None, validation_alias="targetPopulation", serialization_alias="targetPopulation")
