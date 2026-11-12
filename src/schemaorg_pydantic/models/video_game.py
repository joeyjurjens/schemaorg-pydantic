from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .game import Game
from .software_application import SoftwareApplication
from .game_play_mode import GamePlayMode

if TYPE_CHECKING:
    from .creative_work import CreativeWork
    from .game_server import GameServer
    from .music_group import MusicGroup
    from .performing_group import PerformingGroup
    from .person import Person
    from .thing import Thing
    from .video_object import VideoObject

if TYPE_CHECKING:
    CreativeWork_Ref = Union[CreativeWork, Ref]
else:
    CreativeWork_Ref = Union[Is["CreativeWork"], Ref]

if TYPE_CHECKING:
    GameServer_Ref = Union[GameServer, Ref]
else:
    GameServer_Ref = Union[Is["GameServer"], Ref]

if TYPE_CHECKING:
    MusicGroup_Person_Ref = Union[MusicGroup, Person, Ref]
else:
    MusicGroup_Person_Ref = Union[Is["MusicGroup"], Is["Person"], Ref]

if TYPE_CHECKING:
    PerformingGroup_Person_Ref = Union[PerformingGroup, Person, Ref]
else:
    PerformingGroup_Person_Ref = Union[Is["PerformingGroup"], Is["Person"], Ref]

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]

if TYPE_CHECKING:
    Thing_Text_Ref = Union[Thing, Text, Ref]
else:
    Thing_Text_Ref = Union[Is["Thing"], Text, Ref]

if TYPE_CHECKING:
    VideoObject_Ref = Union[VideoObject, Ref]
else:
    VideoObject_Ref = Union[Is["VideoObject"], Ref]


class VideoGame(Game, SoftwareApplication):
    """A video game is an electronic game that involves human interaction with a user interface to generate visual feedback on a video device."""
    schema_type: ClassVar[str] = "VideoGame"
    actor: PerformingGroup_Person_Ref | list[PerformingGroup_Person_Ref] | None = Field(default=None)
    cheat_code: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="cheatCode", serialization_alias="cheatCode")
    director: Person_Ref | list[Person_Ref] | None = Field(default=None)
    game_edition: Text | list[Text] | None = Field(default=None, validation_alias="gameEdition", serialization_alias="gameEdition")
    game_platform: Thing_Text_Ref | list[Thing_Text_Ref] | None = Field(default=None, validation_alias="gamePlatform", serialization_alias="gamePlatform")
    game_server: GameServer_Ref | list[GameServer_Ref] | None = Field(default=None, validation_alias="gameServer", serialization_alias="gameServer")
    game_tip: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="gameTip", serialization_alias="gameTip")
    music_by: MusicGroup_Person_Ref | list[MusicGroup_Person_Ref] | None = Field(default=None, validation_alias="musicBy", serialization_alias="musicBy")
    play_mode: GamePlayMode | list[GamePlayMode] | None = Field(default=None, validation_alias="playMode", serialization_alias="playMode")
    trailer: VideoObject_Ref | list[VideoObject_Ref] | None = Field(default=None)
