from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .trip import Trip

if TYPE_CHECKING:
    from .boat_terminal import BoatTerminal

if TYPE_CHECKING:
    BoatTerminal_Ref = Union[BoatTerminal, Ref]
else:
    BoatTerminal_Ref = Union[Is["BoatTerminal"], Ref]


class BoatTrip(Trip):
    """A trip on a commercial ferry line."""
    schema_type: ClassVar[str] = "BoatTrip"
    arrival_boat_terminal: BoatTerminal_Ref | list[BoatTerminal_Ref] | None = Field(default=None, validation_alias="arrivalBoatTerminal", serialization_alias="arrivalBoatTerminal")
    departure_boat_terminal: BoatTerminal_Ref | list[BoatTerminal_Ref] | None = Field(default=None, validation_alias="departureBoatTerminal", serialization_alias="departureBoatTerminal")
