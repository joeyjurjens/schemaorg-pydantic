from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .event import Event

if TYPE_CHECKING:
    from .person import Person
    from .sports_team import SportsTeam

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]

if TYPE_CHECKING:
    Person_SportsTeam_Ref = Union[Person, SportsTeam, Ref]
else:
    Person_SportsTeam_Ref = Union[Is["Person"], Is["SportsTeam"], Ref]


class SportsEvent(Event):
    """Event type: Sports event."""
    schema_type: ClassVar[str] = "SportsEvent"
    away_team: Person_SportsTeam_Ref | list[Person_SportsTeam_Ref] | None = Field(default=None, validation_alias="awayTeam", serialization_alias="awayTeam")
    competitor: Person_SportsTeam_Ref | list[Person_SportsTeam_Ref] | None = Field(default=None)
    home_team: Person_SportsTeam_Ref | list[Person_SportsTeam_Ref] | None = Field(default=None, validation_alias="homeTeam", serialization_alias="homeTeam")
    referee: Person_Ref | list[Person_Ref] | None = Field(default=None)
    sport: Text | list[Text] | None = Field(default=None)
