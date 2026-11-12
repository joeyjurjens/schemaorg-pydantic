from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .medical_procedure import MedicalProcedure

if TYPE_CHECKING:
    from .dose_schedule import DoseSchedule
    from .drug import Drug
    from .medical_entity import MedicalEntity

if TYPE_CHECKING:
    DoseSchedule_Ref = Union[DoseSchedule, Ref]
else:
    DoseSchedule_Ref = Union[Is["DoseSchedule"], Ref]

if TYPE_CHECKING:
    Drug_Ref = Union[Drug, Ref]
else:
    Drug_Ref = Union[Is["Drug"], Ref]

if TYPE_CHECKING:
    MedicalEntity_Ref = Union[MedicalEntity, Ref]
else:
    MedicalEntity_Ref = Union[Is["MedicalEntity"], Ref]


class TherapeuticProcedure(MedicalProcedure):
    """A medical procedure intended primarily for therapeutic purposes, aimed at improving a health condition."""
    schema_type: ClassVar[str] = "TherapeuticProcedure"
    adverse_outcome: MedicalEntity_Ref | list[MedicalEntity_Ref] | None = Field(default=None, validation_alias="adverseOutcome", serialization_alias="adverseOutcome")
    dose_schedule: DoseSchedule_Ref | list[DoseSchedule_Ref] | None = Field(default=None, validation_alias="doseSchedule", serialization_alias="doseSchedule")
    drug: Drug_Ref | list[Drug_Ref] | None = Field(default=None)
