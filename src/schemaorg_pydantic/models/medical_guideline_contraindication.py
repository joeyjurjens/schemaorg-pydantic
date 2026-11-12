from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_guideline import MedicalGuideline


class MedicalGuidelineContraindication(MedicalGuideline):
    """A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound."""
    schema_type: ClassVar[str] = "MedicalGuidelineContraindication"
