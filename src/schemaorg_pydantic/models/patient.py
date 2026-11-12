from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .medical_audience import MedicalAudience
from .person import Person

if TYPE_CHECKING:
    from .drug import Drug
    from .medical_condition import MedicalCondition

if TYPE_CHECKING:
    Drug_Ref = Union[Drug, Ref]
else:
    Drug_Ref = Union[Is["Drug"], Ref]

if TYPE_CHECKING:
    MedicalCondition_Ref = Union[MedicalCondition, Ref]
else:
    MedicalCondition_Ref = Union[Is["MedicalCondition"], Ref]


class Patient(MedicalAudience, Person):
    """A patient is any person recipient of health care services."""
    schema_type: ClassVar[str] = "Patient"
    diagnosis: MedicalCondition_Ref | list[MedicalCondition_Ref] | None = Field(default=None)
    drug: Drug_Ref | list[Drug_Ref] | None = Field(default=None)
