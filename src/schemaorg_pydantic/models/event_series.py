from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event
from .series import Series


class EventSeries(Event, Series):
    """A series of [[Event]]s. Included events can relate with the series using the [[superEvent]] property."""
    schema_type: ClassVar[str] = "EventSeries"
