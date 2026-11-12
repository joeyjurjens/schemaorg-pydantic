from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_business import MedicalBusiness


class Optician(MedicalBusiness):
    """A store that sells reading glasses and similar devices for improving vision."""
    schema_type: ClassVar[str] = "Optician"
