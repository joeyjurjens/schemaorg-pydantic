from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure
from .organization import Organization


class EducationalOrganization(CivicStructure, Organization):
    """An educational organization."""
    schema_type: ClassVar[str] = "EducationalOrganization"
