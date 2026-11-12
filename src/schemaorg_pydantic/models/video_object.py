from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .media_object import MediaObject

if TYPE_CHECKING:
    from .music_group import MusicGroup
    from .performing_group import PerformingGroup
    from .person import Person

if TYPE_CHECKING:
    MediaObject_Text_Ref = Union[MediaObject, Text, Ref]
else:
    MediaObject_Text_Ref = Union[Is["MediaObject"], Text, Ref]

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


class VideoObject(MediaObject):
    """A video file."""
    schema_type: ClassVar[str] = "VideoObject"
    actor: PerformingGroup_Person_Ref | list[PerformingGroup_Person_Ref] | None = Field(default=None)
    caption: MediaObject_Text_Ref | list[MediaObject_Text_Ref] | None = Field(default=None)
    director: Person_Ref | list[Person_Ref] | None = Field(default=None)
    embedded_text_caption: Text | list[Text] | None = Field(default=None, validation_alias="embeddedTextCaption", serialization_alias="embeddedTextCaption")
    music_by: MusicGroup_Person_Ref | list[MusicGroup_Person_Ref] | None = Field(default=None, validation_alias="musicBy", serialization_alias="musicBy")
    transcript: Text | list[Text] | None = Field(default=None)
    video_frame_size: Text | list[Text] | None = Field(default=None, validation_alias="videoFrameSize", serialization_alias="videoFrameSize")
    video_quality: Text | list[Text] | None = Field(default=None, validation_alias="videoQuality", serialization_alias="videoQuality")
