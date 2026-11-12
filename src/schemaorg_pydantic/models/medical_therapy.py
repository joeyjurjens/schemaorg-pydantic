from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .therapeutic_procedure import TherapeuticProcedure

if TYPE_CHECKING:
    from .medical_contraindication import MedicalContraindication
    from .medical_entity import MedicalEntity

if TYPE_CHECKING:
    MedicalContraindication_Text_Ref = Union[MedicalContraindication, Text, Ref]
else:
    MedicalContraindication_Text_Ref = Union[Is["MedicalContraindication"], Text, Ref]

if TYPE_CHECKING:
    MedicalEntity_Ref = Union[MedicalEntity, Ref]
else:
    MedicalEntity_Ref = Union[Is["MedicalEntity"], Ref]

if TYPE_CHECKING:
    MedicalTherapy_Ref = Union["MedicalTherapy", Ref]
else:
    MedicalTherapy_Ref = Union[Is["MedicalTherapy"], Ref]


class MedicalTherapy(TherapeuticProcedure):
    """Any medical intervention designed to prevent, treat, and cure human diseases and medical conditions, including both curative and palliative therapies. Medical therapies are typically processes of care relying upon pharmacotherapy, behavioral therapy, supportive therapy (with fluid or nutrition for example), or detoxification (e.g. hemodialysis) aimed at improving or preventing a health condition."""
    schema_type: ClassVar[str] = "MedicalTherapy"
    contraindication: MedicalContraindication_Text_Ref | list[MedicalContraindication_Text_Ref] | None = Field(default=None)
    duplicate_therapy: MedicalTherapy_Ref | list[MedicalTherapy_Ref] | None = Field(default=None, validation_alias="duplicateTherapy", serialization_alias="duplicateTherapy")
    serious_adverse_outcome: MedicalEntity_Ref | list[MedicalEntity_Ref] | None = Field(default=None, validation_alias="seriousAdverseOutcome", serialization_alias="seriousAdverseOutcome")
