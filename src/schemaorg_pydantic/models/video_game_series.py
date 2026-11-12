from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref, Text, Url
from .creative_work_series import CreativeWorkSeries
from .game_play_mode import GamePlayMode

if TYPE_CHECKING:
    from .creative_work import CreativeWork
    from .creative_work_season import CreativeWorkSeason
    from .episode import Episode
    from .music_group import MusicGroup
    from .organization import Organization
    from .performing_group import PerformingGroup
    from .person import Person
    from .place import Place
    from .postal_address import PostalAddress
    from .quantitative_value import QuantitativeValue
    from .thing import Thing
    from .video_object import VideoObject

if TYPE_CHECKING:
    CreativeWork_Ref = Union[CreativeWork, Ref]
else:
    CreativeWork_Ref = Union[Is["CreativeWork"], Ref]

if TYPE_CHECKING:
    CreativeWorkSeason_Ref = Union[CreativeWorkSeason, Ref]
else:
    CreativeWorkSeason_Ref = Union[Is["CreativeWorkSeason"], Ref]

if TYPE_CHECKING:
    Episode_Ref = Union[Episode, Ref]
else:
    Episode_Ref = Union[Is["Episode"], Ref]

if TYPE_CHECKING:
    MusicGroup_Person_Ref = Union[MusicGroup, Person, Ref]
else:
    MusicGroup_Person_Ref = Union[Is["MusicGroup"], Is["Person"], Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]

if TYPE_CHECKING:
    PerformingGroup_Person_Ref = Union[PerformingGroup, Person, Ref]
else:
    PerformingGroup_Person_Ref = Union[Is["PerformingGroup"], Is["Person"], Ref]

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]

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

if TYPE_CHECKING:
    Thing_Text_Ref = Union[Thing, Text, Ref]
else:
    Thing_Text_Ref = Union[Is["Thing"], Text, Ref]

if TYPE_CHECKING:
    VideoObject_Ref = Union[VideoObject, Ref]
else:
    VideoObject_Ref = Union[Is["VideoObject"], Ref]


class VideoGameSeries(CreativeWorkSeries):
    """A video game series."""
    schema_type: ClassVar[str] = "VideoGameSeries"
    actor: PerformingGroup_Person_Ref | list[PerformingGroup_Person_Ref] | None = Field(default=None)
    character_attribute: Thing_Ref | list[Thing_Ref] | None = Field(default=None, validation_alias="characterAttribute", serialization_alias="characterAttribute")
    cheat_code: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="cheatCode", serialization_alias="cheatCode")
    contains_season: CreativeWorkSeason_Ref | list[CreativeWorkSeason_Ref] | None = Field(default=None, validation_alias="containsSeason", serialization_alias="containsSeason")
    director: Person_Ref | list[Person_Ref] | None = Field(default=None)
    episode: Episode_Ref | list[Episode_Ref] | None = Field(default=None)
    game_item: Thing_Ref | list[Thing_Ref] | None = Field(default=None, validation_alias="gameItem", serialization_alias="gameItem")
    game_location: Place_PostalAddress_Url_Ref | list[Place_PostalAddress_Url_Ref] | None = Field(default=None, validation_alias="gameLocation", serialization_alias="gameLocation")
    game_platform: Thing_Text_Ref | list[Thing_Text_Ref] | None = Field(default=None, validation_alias="gamePlatform", serialization_alias="gamePlatform")
    music_by: MusicGroup_Person_Ref | list[MusicGroup_Person_Ref] | None = Field(default=None, validation_alias="musicBy", serialization_alias="musicBy")
    number_of_episodes: Integer | list[Integer] | None = Field(default=None, validation_alias="numberOfEpisodes", serialization_alias="numberOfEpisodes")
    number_of_players: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="numberOfPlayers", serialization_alias="numberOfPlayers")
    number_of_seasons: Integer | list[Integer] | None = Field(default=None, validation_alias="numberOfSeasons", serialization_alias="numberOfSeasons")
    play_mode: GamePlayMode | list[GamePlayMode] | None = Field(default=None, validation_alias="playMode", serialization_alias="playMode")
    production_company: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="productionCompany", serialization_alias="productionCompany")
    quest: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    trailer: VideoObject_Ref | list[VideoObject_Ref] | None = Field(default=None)
