from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class GovernmentBuilding(CivicStructure):
    """A government building."""
    schema_type: ClassVar[str] = "GovernmentBuilding"
