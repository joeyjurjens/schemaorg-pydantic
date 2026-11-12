from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .reservation import Reservation


class EventReservation(Reservation):
    """A reservation for an event like a concert, sporting event, or lecture."""
    schema_type: ClassVar[str] = "EventReservation"
