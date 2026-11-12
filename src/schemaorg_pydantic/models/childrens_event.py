from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event


class ChildrensEvent(Event):
    """Event type: Children's event."""
    schema_type: ClassVar[str] = "ChildrensEvent"
