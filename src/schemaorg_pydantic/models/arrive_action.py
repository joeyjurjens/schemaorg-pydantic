from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .move_action import MoveAction


class ArriveAction(MoveAction):
    """The act of arriving at a place. An agent arrives at a destination from a fromLocation, optionally with participants."""
    schema_type: ClassVar[str] = "ArriveAction"
