from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .reservation import Reservation


class BusReservation(Reservation):
    """A reservation for bus travel."""
    schema_type: ClassVar[str] = "BusReservation"
