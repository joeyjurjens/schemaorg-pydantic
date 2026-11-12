from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Number
from .intangible import Intangible


class OccupationalExperienceRequirements(Intangible):
    """Indicates employment-related experience requirements, e.g. [[monthsOfExperience]]."""
    schema_type: ClassVar[str] = "OccupationalExperienceRequirements"
    months_of_experience: Number | list[Number] | None = Field(default=None, validation_alias="monthsOfExperience", serialization_alias="monthsOfExperience")
