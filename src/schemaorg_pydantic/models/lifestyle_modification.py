from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_entity import MedicalEntity


class LifestyleModification(MedicalEntity):
    """A process of care involving exercise, changes to diet, fitness routines, and other lifestyle changes aimed at improving a health condition."""
    schema_type: ClassVar[str] = "LifestyleModification"
