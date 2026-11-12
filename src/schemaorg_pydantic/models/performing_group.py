from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organization import Organization


class PerformingGroup(Organization):
    """A performance group, such as a band, an orchestra, or a circus."""
    schema_type: ClassVar[str] = "PerformingGroup"
