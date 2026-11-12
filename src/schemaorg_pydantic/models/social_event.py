from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event


class SocialEvent(Event):
    """Event type: Social event."""
    schema_type: ClassVar[str] = "SocialEvent"
