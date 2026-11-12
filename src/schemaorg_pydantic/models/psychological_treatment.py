from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .therapeutic_procedure import TherapeuticProcedure


class PsychologicalTreatment(TherapeuticProcedure):
    """A process of care relying upon counseling, dialogue and communication  aimed at improving a mental health condition without use of drugs."""
    schema_type: ClassVar[str] = "PsychologicalTreatment"
