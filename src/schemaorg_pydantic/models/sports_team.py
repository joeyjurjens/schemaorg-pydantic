from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .sports_organization import SportsOrganization
from .gender_type import GenderType

if TYPE_CHECKING:
    from .person import Person

GenderType_Text = Union[GenderType, Text]
if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]


class SportsTeam(SportsOrganization):
    """Organization: Sports team."""
    schema_type: ClassVar[str] = "SportsTeam"
    athlete: Person_Ref | list[Person_Ref] | None = Field(default=None)
    coach: Person_Ref | list[Person_Ref] | None = Field(default=None)
    gender: GenderType_Text | list[GenderType_Text] | None = Field(default=None)
