from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Url
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .place import Place
    from .postal_address import PostalAddress
    from .quantitative_value import QuantitativeValue
    from .thing import Thing

if TYPE_CHECKING:
    Place_PostalAddress_Url_Ref = Union[Place, PostalAddress, Url, Ref]
else:
    Place_PostalAddress_Url_Ref = Union[Is["Place"], Is["PostalAddress"], Url, Ref]

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]


class Game(CreativeWork):
    """The Game type represents things which are games. These are typically rule-governed recreational activities, e.g. role-playing games in which players assume the role of characters in a fictional setting."""
    schema_type: ClassVar[str] = "Game"
    character_attribute: Thing_Ref | list[Thing_Ref] | None = Field(default=None, validation_alias="characterAttribute", serialization_alias="characterAttribute")
    game_item: Thing_Ref | list[Thing_Ref] | None = Field(default=None, validation_alias="gameItem", serialization_alias="gameItem")
    game_location: Place_PostalAddress_Url_Ref | list[Place_PostalAddress_Url_Ref] | None = Field(default=None, validation_alias="gameLocation", serialization_alias="gameLocation")
    number_of_players: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="numberOfPlayers", serialization_alias="numberOfPlayers")
    quest: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
