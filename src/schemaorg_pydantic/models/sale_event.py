from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event


class SaleEvent(Event):
    """Event type: Sales event."""
    schema_type: ClassVar[str] = "SaleEvent"
