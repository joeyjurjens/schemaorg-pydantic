from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .medical_business import MedicalBusiness
from .medical_organization import MedicalOrganization

if TYPE_CHECKING:
    from .category_code import CategoryCode
    from .hospital import Hospital
    from .medical_procedure import MedicalProcedure
    from .medical_test import MedicalTest
    from .medical_therapy import MedicalTherapy

if TYPE_CHECKING:
    CategoryCode_Text_Ref = Union[CategoryCode, Text, Ref]
else:
    CategoryCode_Text_Ref = Union[Is["CategoryCode"], Text, Ref]

if TYPE_CHECKING:
    Hospital_Ref = Union[Hospital, Ref]
else:
    Hospital_Ref = Union[Is["Hospital"], Ref]

if TYPE_CHECKING:
    MedicalProcedure_MedicalTest_MedicalTherapy_Ref = Union[MedicalProcedure, MedicalTest, MedicalTherapy, Ref]
else:
    MedicalProcedure_MedicalTest_MedicalTherapy_Ref = Union[Is["MedicalProcedure"], Is["MedicalTest"], Is["MedicalTherapy"], Ref]


class Physician(MedicalBusiness, MedicalOrganization):
    """An individual physician or a physician's office considered as a [[MedicalOrganization]]."""
    schema_type: ClassVar[str] = "Physician"
    available_service: MedicalProcedure_MedicalTest_MedicalTherapy_Ref | list[MedicalProcedure_MedicalTest_MedicalTherapy_Ref] | None = Field(default=None, validation_alias="availableService", serialization_alias="availableService")
    hospital_affiliation: Hospital_Ref | list[Hospital_Ref] | None = Field(default=None, validation_alias="hospitalAffiliation", serialization_alias="hospitalAffiliation")
    occupational_category: CategoryCode_Text_Ref | list[CategoryCode_Text_Ref] | None = Field(default=None, validation_alias="occupationalCategory", serialization_alias="occupationalCategory")
    us_npi: Text | list[Text] | None = Field(default=None, validation_alias="usNPI", serialization_alias="usNPI")
