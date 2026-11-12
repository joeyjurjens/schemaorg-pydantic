from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_entity import MedicalEntity


class MedicalIntangible(MedicalEntity):
    """A utility class that serves as the umbrella for a number of 'intangible' things in the medical space."""
    schema_type: ClassVar[str] = "MedicalIntangible"
