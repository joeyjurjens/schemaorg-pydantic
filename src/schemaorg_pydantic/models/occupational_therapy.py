from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_therapy import MedicalTherapy


class OccupationalTherapy(MedicalTherapy):
    """A treatment of people with physical, emotional, or social problems, using purposeful activity to help them overcome or learn to deal with their problems."""
    schema_type: ClassVar[str] = "OccupationalTherapy"
