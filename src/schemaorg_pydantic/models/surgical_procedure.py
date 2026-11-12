from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_procedure import MedicalProcedure


class SurgicalProcedure(MedicalProcedure):
    """A medical procedure involving an incision with instruments; performed for diagnose, or therapeutic purposes."""
    schema_type: ClassVar[str] = "SurgicalProcedure"
