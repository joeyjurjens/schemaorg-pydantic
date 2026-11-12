from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .medical_test import MedicalTest

if TYPE_CHECKING:
    MedicalTest_Ref = Union[MedicalTest, Ref]
else:
    MedicalTest_Ref = Union[Is["MedicalTest"], Ref]


class MedicalTestPanel(MedicalTest):
    """Any collection of tests commonly ordered together."""
    schema_type: ClassVar[str] = "MedicalTestPanel"
    sub_test: MedicalTest_Ref | list[MedicalTest_Ref] | None = Field(default=None, validation_alias="subTest", serialization_alias="subTest")
