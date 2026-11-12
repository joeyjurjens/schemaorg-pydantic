from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .medical_guideline import MedicalGuideline


class MedicalGuidelineRecommendation(MedicalGuideline):
    """A guideline recommendation that is regarded as efficacious and where quality of the data supporting the recommendation is sound."""
    schema_type: ClassVar[str] = "MedicalGuidelineRecommendation"
    recommendation_strength: Text | list[Text] | None = Field(default=None, validation_alias="recommendationStrength", serialization_alias="recommendationStrength")
