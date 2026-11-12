from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .civic_structure import CivicStructure
from .emergency_service import EmergencyService
from .medical_organization import MedicalOrganization

if TYPE_CHECKING:
    from .cdcpmd_record import CDCPMDRecord
    from .dataset import Dataset
    from .medical_procedure import MedicalProcedure
    from .medical_test import MedicalTest
    from .medical_therapy import MedicalTherapy

if TYPE_CHECKING:
    CDCPMDRecord_Dataset_Ref = Union[CDCPMDRecord, Dataset, Ref]
else:
    CDCPMDRecord_Dataset_Ref = Union[Is["CDCPMDRecord"], Is["Dataset"], Ref]

if TYPE_CHECKING:
    MedicalProcedure_MedicalTest_MedicalTherapy_Ref = Union[MedicalProcedure, MedicalTest, MedicalTherapy, Ref]
else:
    MedicalProcedure_MedicalTest_MedicalTherapy_Ref = Union[Is["MedicalProcedure"], Is["MedicalTest"], Is["MedicalTherapy"], Ref]


class Hospital(CivicStructure, EmergencyService, MedicalOrganization):
    """A hospital."""
    schema_type: ClassVar[str] = "Hospital"
    available_service: MedicalProcedure_MedicalTest_MedicalTherapy_Ref | list[MedicalProcedure_MedicalTest_MedicalTherapy_Ref] | None = Field(default=None, validation_alias="availableService", serialization_alias="availableService")
    healthcare_reporting_data: CDCPMDRecord_Dataset_Ref | list[CDCPMDRecord_Dataset_Ref] | None = Field(default=None, validation_alias="healthcareReportingData", serialization_alias="healthcareReportingData")
