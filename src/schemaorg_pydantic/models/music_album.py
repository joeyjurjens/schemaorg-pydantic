from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .music_playlist import MusicPlaylist
from .music_album_production_type import MusicAlbumProductionType
from .music_album_release_type import MusicAlbumReleaseType

if TYPE_CHECKING:
    from .music_group import MusicGroup
    from .music_release import MusicRelease
    from .person import Person

if TYPE_CHECKING:
    MusicGroup_Person_Ref = Union[MusicGroup, Person, Ref]
else:
    MusicGroup_Person_Ref = Union[Is["MusicGroup"], Is["Person"], Ref]

if TYPE_CHECKING:
    MusicRelease_Ref = Union[MusicRelease, Ref]
else:
    MusicRelease_Ref = Union[Is["MusicRelease"], Ref]


class MusicAlbum(MusicPlaylist):
    """A collection of music tracks."""
    schema_type: ClassVar[str] = "MusicAlbum"
    album_production_type: MusicAlbumProductionType | list[MusicAlbumProductionType] | None = Field(default=None, validation_alias="albumProductionType", serialization_alias="albumProductionType")
    album_release: MusicRelease_Ref | list[MusicRelease_Ref] | None = Field(default=None, validation_alias="albumRelease", serialization_alias="albumRelease")
    album_release_type: MusicAlbumReleaseType | list[MusicAlbumReleaseType] | None = Field(default=None, validation_alias="albumReleaseType", serialization_alias="albumReleaseType")
    by_artist: MusicGroup_Person_Ref | list[MusicGroup_Person_Ref] | None = Field(default=None, validation_alias="byArtist", serialization_alias="byArtist")
