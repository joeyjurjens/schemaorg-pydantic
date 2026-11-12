from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organization import Organization


class SearchRescueOrganization(Organization):
    """A Search and Rescue organization of some kind."""
    schema_type: ClassVar[str] = "SearchRescueOrganization"
