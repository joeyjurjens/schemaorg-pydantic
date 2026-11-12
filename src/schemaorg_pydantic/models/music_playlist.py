from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .item_list import ItemList
    from .music_recording import MusicRecording

if TYPE_CHECKING:
    ItemList_MusicRecording_Ref = Union[ItemList, MusicRecording, Ref]
else:
    ItemList_MusicRecording_Ref = Union[Is["ItemList"], Is["MusicRecording"], Ref]


class MusicPlaylist(CreativeWork):
    """A collection of music tracks in playlist form."""
    schema_type: ClassVar[str] = "MusicPlaylist"
    num_tracks: Integer | list[Integer] | None = Field(default=None, validation_alias="numTracks", serialization_alias="numTracks")
    track: ItemList_MusicRecording_Ref | list[ItemList_MusicRecording_Ref] | None = Field(default=None)
