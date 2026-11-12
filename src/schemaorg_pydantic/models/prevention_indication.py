from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_indication import MedicalIndication


class PreventionIndication(MedicalIndication):
    """An indication for preventing an underlying condition, symptom, etc."""
    schema_type: ClassVar[str] = "PreventionIndication"
