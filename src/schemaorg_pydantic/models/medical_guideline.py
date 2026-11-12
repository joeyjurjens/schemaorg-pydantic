from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, Is, Ref, Text
from .medical_entity import MedicalEntity
from .medical_evidence_level import MedicalEvidenceLevel

if TYPE_CHECKING:
    MedicalEntity_Ref = Union[MedicalEntity, Ref]
else:
    MedicalEntity_Ref = Union[Is["MedicalEntity"], Ref]


class MedicalGuideline(MedicalEntity):
    """Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement that denotes how to diagnose and treat a particular condition. Note: this type should be used to tag the actual guideline recommendation; if the guideline recommendation occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall article, not this type. Note also: the organization making the recommendation should be captured in the recognizingAuthority base property of MedicalEntity."""
    schema_type: ClassVar[str] = "MedicalGuideline"
    evidence_level: MedicalEvidenceLevel | list[MedicalEvidenceLevel] | None = Field(default=None, validation_alias="evidenceLevel", serialization_alias="evidenceLevel")
    evidence_origin: Text | list[Text] | None = Field(default=None, validation_alias="evidenceOrigin", serialization_alias="evidenceOrigin")
    guideline_date: Date | list[Date] | None = Field(default=None, validation_alias="guidelineDate", serialization_alias="guidelineDate")
    guideline_subject: MedicalEntity_Ref | list[MedicalEntity_Ref] | None = Field(default=None, validation_alias="guidelineSubject", serialization_alias="guidelineSubject")
