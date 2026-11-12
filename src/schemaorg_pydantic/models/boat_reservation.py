from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .reservation import Reservation


class BoatReservation(Reservation):
    """A reservation for boat travel."""
    schema_type: ClassVar[str] = "BoatReservation"
