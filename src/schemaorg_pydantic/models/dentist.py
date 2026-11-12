from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_business import MedicalBusiness
from .medical_organization import MedicalOrganization


class Dentist(MedicalBusiness, MedicalOrganization):
    """A dentist."""
    schema_type: ClassVar[str] = "Dentist"
