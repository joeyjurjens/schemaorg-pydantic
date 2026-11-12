from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event


class LiteraryEvent(Event):
    """Event type: Literary event."""
    schema_type: ClassVar[str] = "LiteraryEvent"
