from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .medical_intangible import MedicalIntangible

if TYPE_CHECKING:
    from .medical_condition import MedicalCondition
    from .medical_sign_or_symptom import MedicalSignOrSymptom

if TYPE_CHECKING:
    MedicalCondition_Ref = Union[MedicalCondition, Ref]
else:
    MedicalCondition_Ref = Union[Is["MedicalCondition"], Ref]

if TYPE_CHECKING:
    MedicalSignOrSymptom_Ref = Union[MedicalSignOrSymptom, Ref]
else:
    MedicalSignOrSymptom_Ref = Union[Is["MedicalSignOrSymptom"], Ref]


class DDxElement(MedicalIntangible):
    """An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it."""
    schema_type: ClassVar[str] = "DDxElement"
    diagnosis: MedicalCondition_Ref | list[MedicalCondition_Ref] | None = Field(default=None)
    distinguishing_sign: MedicalSignOrSymptom_Ref | list[MedicalSignOrSymptom_Ref] | None = Field(default=None, validation_alias="distinguishingSign", serialization_alias="distinguishingSign")
