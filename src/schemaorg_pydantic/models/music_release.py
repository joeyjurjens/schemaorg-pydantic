from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .music_playlist import MusicPlaylist
from .music_release_format_type import MusicReleaseFormatType

if TYPE_CHECKING:
    from .music_album import MusicAlbum
    from .organization import Organization
    from .person import Person
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    MusicAlbum_Ref = Union[MusicAlbum, Ref]
else:
    MusicAlbum_Ref = Union[Is["MusicAlbum"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class MusicRelease(MusicPlaylist):
    """A MusicRelease is a specific release of a music album."""
    schema_type: ClassVar[str] = "MusicRelease"
    catalog_number: Text | list[Text] | None = Field(default=None, validation_alias="catalogNumber", serialization_alias="catalogNumber")
    credited_to: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="creditedTo", serialization_alias="creditedTo")
    duration: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    music_release_format: MusicReleaseFormatType | list[MusicReleaseFormatType] | None = Field(default=None, validation_alias="musicReleaseFormat", serialization_alias="musicReleaseFormat")
    record_label: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="recordLabel", serialization_alias="recordLabel")
    release_of: MusicAlbum_Ref | list[MusicAlbum_Ref] | None = Field(default=None, validation_alias="releaseOf", serialization_alias="releaseOf")
