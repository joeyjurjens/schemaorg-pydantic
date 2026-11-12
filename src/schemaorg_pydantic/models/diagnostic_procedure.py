from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_procedure import MedicalProcedure


class DiagnosticProcedure(MedicalProcedure):
    """A medical procedure intended primarily for diagnostic, as opposed to therapeutic, purposes."""
    schema_type: ClassVar[str] = "DiagnosticProcedure"
