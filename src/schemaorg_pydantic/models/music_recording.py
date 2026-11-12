from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .music_album import MusicAlbum
    from .music_composition import MusicComposition
    from .music_group import MusicGroup
    from .music_playlist import MusicPlaylist
    from .person import Person
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    MusicAlbum_Ref = Union[MusicAlbum, Ref]
else:
    MusicAlbum_Ref = Union[Is["MusicAlbum"], Ref]

if TYPE_CHECKING:
    MusicComposition_Ref = Union[MusicComposition, Ref]
else:
    MusicComposition_Ref = Union[Is["MusicComposition"], Ref]

if TYPE_CHECKING:
    MusicGroup_Person_Ref = Union[MusicGroup, Person, Ref]
else:
    MusicGroup_Person_Ref = Union[Is["MusicGroup"], Is["Person"], Ref]

if TYPE_CHECKING:
    MusicPlaylist_Ref = Union[MusicPlaylist, Ref]
else:
    MusicPlaylist_Ref = Union[Is["MusicPlaylist"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class MusicRecording(CreativeWork):
    """A music recording (track), usually a single song."""
    schema_type: ClassVar[str] = "MusicRecording"
    by_artist: MusicGroup_Person_Ref | list[MusicGroup_Person_Ref] | None = Field(default=None, validation_alias="byArtist", serialization_alias="byArtist")
    duration: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    in_album: MusicAlbum_Ref | list[MusicAlbum_Ref] | None = Field(default=None, validation_alias="inAlbum", serialization_alias="inAlbum")
    in_playlist: MusicPlaylist_Ref | list[MusicPlaylist_Ref] | None = Field(default=None, validation_alias="inPlaylist", serialization_alias="inPlaylist")
    isrc_code: Text | list[Text] | None = Field(default=None, validation_alias="isrcCode", serialization_alias="isrcCode")
    recording_of: MusicComposition_Ref | list[MusicComposition_Ref] | None = Field(default=None, validation_alias="recordingOf", serialization_alias="recordingOf")
