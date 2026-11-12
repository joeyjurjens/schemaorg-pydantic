from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event


class ComedyEvent(Event):
    """Event type: Comedy event."""
    schema_type: ClassVar[str] = "ComedyEvent"
