from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .thing import Thing
from .drug_cost_category import DrugCostCategory
from .drug_pregnancy_category import DrugPregnancyCategory
from .drug_prescription_status import DrugPrescriptionStatus
from .infectious_agent_class import InfectiousAgentClass
from .medical_audience_type import MedicalAudienceType
from .medical_device_purpose import MedicalDevicePurpose
from .medical_evidence_level import MedicalEvidenceLevel
from .medical_imaging_technique import MedicalImagingTechnique
from .medical_observational_study_design import MedicalObservationalStudyDesign
from .medical_procedure_type import MedicalProcedureType
from .medical_specialty import MedicalSpecialty
from .medical_study_status import MedicalStudyStatus
from .medical_trial_design import MedicalTrialDesign
from .medicine_system import MedicineSystem
from .physical_exam import PhysicalExam

if TYPE_CHECKING:
    from .drug_legal_status import DrugLegalStatus
    from .grant import Grant
    from .medical_code import MedicalCode
    from .medical_guideline import MedicalGuideline
    from .medical_study import MedicalStudy
    from .organization import Organization

if TYPE_CHECKING:
    R7b3ace65 = Union[DrugCostCategory, DrugLegalStatus, DrugPregnancyCategory, DrugPrescriptionStatus, InfectiousAgentClass, MedicalAudienceType, MedicalDevicePurpose, MedicalEvidenceLevel, MedicalImagingTechnique, MedicalObservationalStudyDesign, MedicalProcedureType, MedicalSpecialty, MedicalStudyStatus, MedicalTrialDesign, MedicineSystem, PhysicalExam, Text, Ref]
else:
    R7b3ace65 = Union[DrugCostCategory, Is["DrugLegalStatus"], DrugPregnancyCategory, DrugPrescriptionStatus, InfectiousAgentClass, MedicalAudienceType, MedicalDevicePurpose, MedicalEvidenceLevel, MedicalImagingTechnique, MedicalObservationalStudyDesign, MedicalProcedureType, MedicalSpecialty, MedicalStudyStatus, MedicalTrialDesign, MedicineSystem, PhysicalExam, Text, Ref]

if TYPE_CHECKING:
    Grant_Ref = Union[Grant, Ref]
else:
    Grant_Ref = Union[Is["Grant"], Ref]

if TYPE_CHECKING:
    MedicalCode_Ref = Union[MedicalCode, Ref]
else:
    MedicalCode_Ref = Union[Is["MedicalCode"], Ref]

if TYPE_CHECKING:
    MedicalGuideline_Ref = Union[MedicalGuideline, Ref]
else:
    MedicalGuideline_Ref = Union[Is["MedicalGuideline"], Ref]

if TYPE_CHECKING:
    MedicalStudy_Ref = Union[MedicalStudy, Ref]
else:
    MedicalStudy_Ref = Union[Is["MedicalStudy"], Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]


class MedicalEntity(Thing):
    """The most generic type of entity related to health and the practice of medicine."""
    schema_type: ClassVar[str] = "MedicalEntity"
    code: MedicalCode_Ref | list[MedicalCode_Ref] | None = Field(default=None)
    funding: Grant_Ref | list[Grant_Ref] | None = Field(default=None)
    guideline: MedicalGuideline_Ref | list[MedicalGuideline_Ref] | None = Field(default=None)
    legal_status: R7b3ace65 | list[R7b3ace65] | None = Field(default=None, validation_alias="legalStatus", serialization_alias="legalStatus")
    medicine_system: MedicineSystem | list[MedicineSystem] | None = Field(default=None, validation_alias="medicineSystem", serialization_alias="medicineSystem")
    recognizing_authority: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="recognizingAuthority", serialization_alias="recognizingAuthority")
    relevant_specialty: MedicalSpecialty | list[MedicalSpecialty] | None = Field(default=None, validation_alias="relevantSpecialty", serialization_alias="relevantSpecialty")
    study: MedicalStudy_Ref | list[MedicalStudy_Ref] | None = Field(default=None)
