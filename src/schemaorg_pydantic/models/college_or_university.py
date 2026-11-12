from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .educational_organization import EducationalOrganization


class CollegeOrUniversity(EducationalOrganization):
    """A college, university, or other third-level educational institution."""
    schema_type: ClassVar[str] = "CollegeOrUniversity"
