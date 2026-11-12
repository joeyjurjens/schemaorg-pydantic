from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .educational_organization import EducationalOrganization


class Preschool(EducationalOrganization):
    """A preschool."""
    schema_type: ClassVar[str] = "Preschool"
