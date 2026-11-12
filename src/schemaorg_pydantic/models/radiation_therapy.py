from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_therapy import MedicalTherapy


class RadiationTherapy(MedicalTherapy):
    """A process of care using radiation aimed at improving a health condition."""
    schema_type: ClassVar[str] = "RadiationTherapy"
