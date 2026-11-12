from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .medical_entity import MedicalEntity

if TYPE_CHECKING:
    from .medical_contraindication import MedicalContraindication

if TYPE_CHECKING:
    MedicalContraindication_Text_Ref = Union[MedicalContraindication, Text, Ref]
else:
    MedicalContraindication_Text_Ref = Union[Is["MedicalContraindication"], Text, Ref]

if TYPE_CHECKING:
    MedicalEntity_Ref = Union[MedicalEntity, Ref]
else:
    MedicalEntity_Ref = Union[Is["MedicalEntity"], Ref]


class MedicalDevice(MedicalEntity):
    """Any object used in a medical capacity, such as to diagnose or treat a patient."""
    schema_type: ClassVar[str] = "MedicalDevice"
    adverse_outcome: MedicalEntity_Ref | list[MedicalEntity_Ref] | None = Field(default=None, validation_alias="adverseOutcome", serialization_alias="adverseOutcome")
    contraindication: MedicalContraindication_Text_Ref | list[MedicalContraindication_Text_Ref] | None = Field(default=None)
    post_op: Text | list[Text] | None = Field(default=None, validation_alias="postOp", serialization_alias="postOp")
    pre_op: Text | list[Text] | None = Field(default=None, validation_alias="preOp", serialization_alias="preOp")
    procedure: Text | list[Text] | None = Field(default=None)
    serious_adverse_outcome: MedicalEntity_Ref | list[MedicalEntity_Ref] | None = Field(default=None, validation_alias="seriousAdverseOutcome", serialization_alias="seriousAdverseOutcome")
