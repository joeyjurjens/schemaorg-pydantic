from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event


class ExhibitionEvent(Event):
    """Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ..."""
    schema_type: ClassVar[str] = "ExhibitionEvent"
