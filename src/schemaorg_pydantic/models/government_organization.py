from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organization import Organization


class GovernmentOrganization(Organization):
    """A governmental organization or agency."""
    schema_type: ClassVar[str] = "GovernmentOrganization"
