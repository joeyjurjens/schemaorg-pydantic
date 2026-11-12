from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_sign_or_symptom import MedicalSignOrSymptom


class MedicalSymptom(MedicalSignOrSymptom):
    """Any complaint sensed and expressed by the patient (therefore defined as subjective)  like stomachache, lower-back pain, or fatigue."""
    schema_type: ClassVar[str] = "MedicalSymptom"
