from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_study import MedicalStudy
from .medical_trial_design import MedicalTrialDesign


class MedicalTrial(MedicalStudy):
    """A medical trial is a type of medical study that uses a scientific process to compare the safety and efficacy of medical therapies or medical procedures. In general, medical trials are controlled and subjects are allocated at random to the different treatment and/or control groups."""
    schema_type: ClassVar[str] = "MedicalTrial"
    trial_design: MedicalTrialDesign | list[MedicalTrialDesign] | None = Field(default=None, validation_alias="trialDesign", serialization_alias="trialDesign")
