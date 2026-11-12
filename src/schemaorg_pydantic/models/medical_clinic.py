from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .medical_business import MedicalBusiness
from .medical_organization import MedicalOrganization

if TYPE_CHECKING:
    from .medical_procedure import MedicalProcedure
    from .medical_test import MedicalTest
    from .medical_therapy import MedicalTherapy

if TYPE_CHECKING:
    MedicalProcedure_MedicalTest_MedicalTherapy_Ref = Union[MedicalProcedure, MedicalTest, MedicalTherapy, Ref]
else:
    MedicalProcedure_MedicalTest_MedicalTherapy_Ref = Union[Is["MedicalProcedure"], Is["MedicalTest"], Is["MedicalTherapy"], Ref]


class MedicalClinic(MedicalBusiness, MedicalOrganization):
    """A facility, often associated with a hospital or medical school, that is devoted to the specific diagnosis and/or healthcare. Previously limited to outpatients but with evolution it may be open to inpatients as well."""
    schema_type: ClassVar[str] = "MedicalClinic"
    available_service: MedicalProcedure_MedicalTest_MedicalTherapy_Ref | list[MedicalProcedure_MedicalTest_MedicalTherapy_Ref] | None = Field(default=None, validation_alias="availableService", serialization_alias="availableService")
