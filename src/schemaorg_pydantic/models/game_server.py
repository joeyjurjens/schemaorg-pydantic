from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref
from .intangible import Intangible
from .game_server_status import GameServerStatus

if TYPE_CHECKING:
    from .video_game import VideoGame

if TYPE_CHECKING:
    VideoGame_Ref = Union[VideoGame, Ref]
else:
    VideoGame_Ref = Union[Is["VideoGame"], Ref]


class GameServer(Intangible):
    """Server that provides game interaction in a multiplayer game."""
    schema_type: ClassVar[str] = "GameServer"
    game: VideoGame_Ref | list[VideoGame_Ref] | None = Field(default=None)
    players_online: Integer | list[Integer] | None = Field(default=None, validation_alias="playersOnline", serialization_alias="playersOnline")
    server_status: GameServerStatus | list[GameServerStatus] | None = Field(default=None, validation_alias="serverStatus", serialization_alias="serverStatus")
