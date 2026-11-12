from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .resort import Resort
from .sports_activity_location import SportsActivityLocation


class SkiResort(Resort, SportsActivityLocation):
    """A ski resort."""
    schema_type: ClassVar[str] = "SkiResort"
