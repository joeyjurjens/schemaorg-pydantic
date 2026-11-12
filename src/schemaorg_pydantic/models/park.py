from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class Park(CivicStructure):
    """A park."""
    schema_type: ClassVar[str] = "Park"
