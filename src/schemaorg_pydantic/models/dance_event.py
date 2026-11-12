from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event


class DanceEvent(Event):
    """Event type: A social dance."""
    schema_type: ClassVar[str] = "DanceEvent"
