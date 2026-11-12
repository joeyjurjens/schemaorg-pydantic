from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import DateTime, Integer, Is, Ref
from .reservation import Reservation

if TYPE_CHECKING:
    from .place import Place
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    Place_Ref = Union[Place, Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Integer_Ref = Union[QuantitativeValue, Integer, Ref]
else:
    QuantitativeValue_Integer_Ref = Union[Is["QuantitativeValue"], Integer, Ref]


class TaxiReservation(Reservation):
    """A reservation for a taxi."""
    schema_type: ClassVar[str] = "TaxiReservation"
    party_size: QuantitativeValue_Integer_Ref | list[QuantitativeValue_Integer_Ref] | None = Field(default=None, validation_alias="partySize", serialization_alias="partySize")
    pickup_location: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="pickupLocation", serialization_alias="pickupLocation")
    pickup_time: DateTime | list[DateTime] | None = Field(default=None, validation_alias="pickupTime", serialization_alias="pickupTime")
