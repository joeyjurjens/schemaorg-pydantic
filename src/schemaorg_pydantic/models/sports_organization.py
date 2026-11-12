from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .organization import Organization


class SportsOrganization(Organization):
    """Represents the collection of all sports organizations, including sports teams, governing bodies, and sports associations."""
    schema_type: ClassVar[str] = "SportsOrganization"
    sport: Text | list[Text] | None = Field(default=None)
