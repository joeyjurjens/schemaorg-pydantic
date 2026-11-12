from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_organization import MedicalOrganization


class VeterinaryCare(MedicalOrganization):
    """A vet's office."""
    schema_type: ClassVar[str] = "VeterinaryCare"
