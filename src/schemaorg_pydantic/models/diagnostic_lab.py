from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .medical_organization import MedicalOrganization

if TYPE_CHECKING:
    from .medical_test import MedicalTest

if TYPE_CHECKING:
    MedicalTest_Ref = Union[MedicalTest, Ref]
else:
    MedicalTest_Ref = Union[Is["MedicalTest"], Ref]


class DiagnosticLab(MedicalOrganization):
    """A medical laboratory that offers on-site or off-site diagnostic services."""
    schema_type: ClassVar[str] = "DiagnosticLab"
    available_test: MedicalTest_Ref | list[MedicalTest_Ref] | None = Field(default=None, validation_alias="availableTest", serialization_alias="availableTest")
