from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .reservation import Reservation


class TrainReservation(Reservation):
    """A reservation for train travel."""
    schema_type: ClassVar[str] = "TrainReservation"
