from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_entity import MedicalEntity


class MedicalIndication(MedicalEntity):
    """A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc."""
    schema_type: ClassVar[str] = "MedicalIndication"
