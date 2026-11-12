from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event


class Festival(Event):
    """Event type: Festival."""
    schema_type: ClassVar[str] = "Festival"
