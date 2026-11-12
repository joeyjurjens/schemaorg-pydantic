from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .educational_organization import EducationalOrganization


class MiddleSchool(EducationalOrganization):
    """A middle school (typically for children aged around 11-14, although this varies somewhat)."""
    schema_type: ClassVar[str] = "MiddleSchool"
