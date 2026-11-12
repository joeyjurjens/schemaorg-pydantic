from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .move_action import MoveAction


class DepartAction(MoveAction):
    """The act of  departing from a place. An agent departs from a fromLocation for a destination, optionally with participants."""
    schema_type: ClassVar[str] = "DepartAction"
