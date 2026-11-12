from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .reservation import Reservation

if TYPE_CHECKING:
    Reservation_Ref = Union[Reservation, Ref]
else:
    Reservation_Ref = Union[Is["Reservation"], Ref]


class ReservationPackage(Reservation):
    """A group of multiple reservations with common values for all sub-reservations."""
    schema_type: ClassVar[str] = "ReservationPackage"
    sub_reservation: Reservation_Ref | list[Reservation_Ref] | None = Field(default=None, validation_alias="subReservation", serialization_alias="subReservation")
