from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event


class ConferenceEvent(Event):
    """Event type: Conference event."""
    schema_type: ClassVar[str] = "ConferenceEvent"
