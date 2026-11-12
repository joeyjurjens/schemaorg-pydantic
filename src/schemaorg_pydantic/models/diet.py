from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .creative_work import CreativeWork
from .lifestyle_modification import LifestyleModification

if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]


class Diet(CreativeWork, LifestyleModification):
    """A strategy of regulating the intake of food to achieve or maintain a specific health-related goal."""
    schema_type: ClassVar[str] = "Diet"
    diet_features: Text | list[Text] | None = Field(default=None, validation_alias="dietFeatures", serialization_alias="dietFeatures")
    endorsers: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    expert_considerations: Text | list[Text] | None = Field(default=None, validation_alias="expertConsiderations", serialization_alias="expertConsiderations")
    physiological_benefits: Text | list[Text] | None = Field(default=None, validation_alias="physiologicalBenefits", serialization_alias="physiologicalBenefits")
    risks: Text | list[Text] | None = Field(default=None)
