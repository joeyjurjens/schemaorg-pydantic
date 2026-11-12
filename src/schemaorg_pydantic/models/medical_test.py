from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .medical_entity import MedicalEntity
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
    from .drug import Drug
    from .medical_condition import MedicalCondition
    from .medical_device import MedicalDevice
    from .medical_sign import MedicalSign

if TYPE_CHECKING:
    Drug_Ref = Union[Drug, Ref]
else:
    Drug_Ref = Union[Is["Drug"], Ref]

Ree91d7a9 = Union[DrugCostCategory, DrugPregnancyCategory, DrugPrescriptionStatus, InfectiousAgentClass, MedicalAudienceType, MedicalDevicePurpose, MedicalEvidenceLevel, MedicalImagingTechnique, MedicalObservationalStudyDesign, MedicalProcedureType, MedicalSpecialty, MedicalStudyStatus, MedicalTrialDesign, MedicineSystem, PhysicalExam, Text]
if TYPE_CHECKING:
    MedicalCondition_Ref = Union[MedicalCondition, Ref]
else:
    MedicalCondition_Ref = Union[Is["MedicalCondition"], Ref]

if TYPE_CHECKING:
    MedicalDevice_Ref = Union[MedicalDevice, Ref]
else:
    MedicalDevice_Ref = Union[Is["MedicalDevice"], Ref]

if TYPE_CHECKING:
    MedicalSign_Ref = Union[MedicalSign, Ref]
else:
    MedicalSign_Ref = Union[Is["MedicalSign"], Ref]


class MedicalTest(MedicalEntity):
    """Any medical test, typically performed for diagnostic purposes."""
    schema_type: ClassVar[str] = "MedicalTest"
    affected_by: Drug_Ref | list[Drug_Ref] | None = Field(default=None, validation_alias="affectedBy", serialization_alias="affectedBy")
    normal_range: Ree91d7a9 | list[Ree91d7a9] | None = Field(default=None, validation_alias="normalRange", serialization_alias="normalRange")
    sign_detected: MedicalSign_Ref | list[MedicalSign_Ref] | None = Field(default=None, validation_alias="signDetected", serialization_alias="signDetected")
    used_to_diagnose: MedicalCondition_Ref | list[MedicalCondition_Ref] | None = Field(default=None, validation_alias="usedToDiagnose", serialization_alias="usedToDiagnose")
    uses_device: MedicalDevice_Ref | list[MedicalDevice_Ref] | None = Field(default=None, validation_alias="usesDevice", serialization_alias="usesDevice")
