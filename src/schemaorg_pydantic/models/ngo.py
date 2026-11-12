from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organization import Organization


class NGO(Organization):
    """Organization: Non-governmental Organization."""
    schema_type: ClassVar[str] = "NGO"
