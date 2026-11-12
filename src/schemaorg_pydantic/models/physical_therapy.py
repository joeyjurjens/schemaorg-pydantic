from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_therapy import MedicalTherapy


class PhysicalTherapy(MedicalTherapy):
    """A process of progressive physical care and rehabilitation aimed at improving a health condition."""
    schema_type: ClassVar[str] = "PhysicalTherapy"
