from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_condition import MedicalCondition


class MedicalSignOrSymptom(MedicalCondition):
    """Any feature associated or not with a medical condition. In medicine a symptom is generally subjective while a sign is objective."""
    schema_type: ClassVar[str] = "MedicalSignOrSymptom"
