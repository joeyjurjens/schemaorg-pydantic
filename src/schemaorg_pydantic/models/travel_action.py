from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .move_action import MoveAction


class TravelAction(MoveAction):
    """The act of traveling from a fromLocation to a destination by a specified mode of transport, optionally with participants."""
    schema_type: ClassVar[str] = "TravelAction"
    distance: Text | list[Text] | None = Field(default=None)
