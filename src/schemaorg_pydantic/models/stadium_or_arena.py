from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure
from .sports_activity_location import SportsActivityLocation


class StadiumOrArena(CivicStructure, SportsActivityLocation):
    """A stadium."""
    schema_type: ClassVar[str] = "StadiumOrArena"
