from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .medical_sign_or_symptom import MedicalSignOrSymptom
from .physical_exam import PhysicalExam

if TYPE_CHECKING:
    from .medical_test import MedicalTest

if TYPE_CHECKING:
    MedicalTest_Ref = Union[MedicalTest, Ref]
else:
    MedicalTest_Ref = Union[Is["MedicalTest"], Ref]


class MedicalSign(MedicalSignOrSymptom):
    """Any physical manifestation of a person's medical condition discoverable by objective diagnostic tests or physical examination."""
    schema_type: ClassVar[str] = "MedicalSign"
    identifying_exam: PhysicalExam | list[PhysicalExam] | None = Field(default=None, validation_alias="identifyingExam", serialization_alias="identifyingExam")
    identifying_test: MedicalTest_Ref | list[MedicalTest_Ref] | None = Field(default=None, validation_alias="identifyingTest", serialization_alias="identifyingTest")
