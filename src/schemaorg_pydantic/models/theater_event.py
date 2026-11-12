from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event


class TheaterEvent(Event):
    """Event type: Theater performance."""
    schema_type: ClassVar[str] = "TheaterEvent"
