from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .sports_activity_location import SportsActivityLocation


class ExerciseGym(SportsActivityLocation):
    """A gym."""
    schema_type: ClassVar[str] = "ExerciseGym"
