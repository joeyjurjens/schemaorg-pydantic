from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_therapy import MedicalTherapy


class PalliativeProcedure(MedicalTherapy):
    """A medical procedure intended primarily for palliative purposes, aimed at relieving the symptoms of an underlying health condition."""
    schema_type: ClassVar[str] = "PalliativeProcedure"
