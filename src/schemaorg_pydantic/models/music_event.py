from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event


class MusicEvent(Event):
    """Event type: Music event."""
    schema_type: ClassVar[str] = "MusicEvent"
