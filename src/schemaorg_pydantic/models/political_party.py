from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organization import Organization


class PoliticalParty(Organization):
    """Organization: Political Party."""
    schema_type: ClassVar[str] = "PoliticalParty"
