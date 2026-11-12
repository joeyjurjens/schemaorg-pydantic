from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_study import MedicalStudy
from .medical_observational_study_design import MedicalObservationalStudyDesign


class MedicalObservationalStudy(MedicalStudy):
    """An observational study is a type of medical study that attempts to infer the possible effect of a treatment through observation of a cohort of subjects over a period of time. In an observational study, the assignment of subjects into treatment groups versus control groups is outside the control of the investigator. This is in contrast with controlled studies, such as the randomized controlled trials represented by MedicalTrial, where each subject is randomly assigned to a treatment group or a control group before the start of the treatment."""
    schema_type: ClassVar[str] = "MedicalObservationalStudy"
    study_design: MedicalObservationalStudyDesign | list[MedicalObservationalStudyDesign] | None = Field(default=None, validation_alias="studyDesign", serialization_alias="studyDesign")
