from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .physician import Physician

if TYPE_CHECKING:
    from .medical_organization import MedicalOrganization

if TYPE_CHECKING:
    MedicalOrganization_Ref = Union[MedicalOrganization, Ref]
else:
    MedicalOrganization_Ref = Union[Is["MedicalOrganization"], Ref]


class IndividualPhysician(Physician):
    """An individual medical practitioner. For their official address use [[address]], for affiliations to hospitals use [[hospitalAffiliation]]. \nThe [[practicesAt]] property can be used to indicate [[MedicalOrganization]] hospitals, clinics, pharmacies etc. where this physician practices."""
    schema_type: ClassVar[str] = "IndividualPhysician"
    practices_at: MedicalOrganization_Ref | list[MedicalOrganization_Ref] | None = Field(default=None, validation_alias="practicesAt", serialization_alias="practicesAt")
