from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event


class VisualArtsEvent(Event):
    """Event type: Visual arts event."""
    schema_type: ClassVar[str] = "VisualArtsEvent"
