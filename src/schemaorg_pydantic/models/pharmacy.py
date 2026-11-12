from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_business import MedicalBusiness
from .medical_organization import MedicalOrganization


class Pharmacy(MedicalBusiness, MedicalOrganization):
    """A pharmacy or drugstore."""
    schema_type: ClassVar[str] = "Pharmacy"
