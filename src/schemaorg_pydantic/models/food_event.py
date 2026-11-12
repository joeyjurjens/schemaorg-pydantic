from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event


class FoodEvent(Event):
    """Event type: Food event."""
    schema_type: ClassVar[str] = "FoodEvent"
