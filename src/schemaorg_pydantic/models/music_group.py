from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .performing_group import PerformingGroup

if TYPE_CHECKING:
    from .defined_term import DefinedTerm
    from .item_list import ItemList
    from .music_album import MusicAlbum
    from .music_recording import MusicRecording

if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]

if TYPE_CHECKING:
    ItemList_MusicRecording_Ref = Union[ItemList, MusicRecording, Ref]
else:
    ItemList_MusicRecording_Ref = Union[Is["ItemList"], Is["MusicRecording"], Ref]

if TYPE_CHECKING:
    MusicAlbum_Ref = Union[MusicAlbum, Ref]
else:
    MusicAlbum_Ref = Union[Is["MusicAlbum"], Ref]


class MusicGroup(PerformingGroup):
    """A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician."""
    schema_type: ClassVar[str] = "MusicGroup"
    album: MusicAlbum_Ref | list[MusicAlbum_Ref] | None = Field(default=None)
    genre: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    track: ItemList_MusicRecording_Ref | list[ItemList_MusicRecording_Ref] | None = Field(default=None)
