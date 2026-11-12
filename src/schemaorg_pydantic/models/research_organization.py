from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organization import Organization


class ResearchOrganization(Organization):
    """A Research Organization (e.g. scientific institute, research company)."""
    schema_type: ClassVar[str] = "ResearchOrganization"
