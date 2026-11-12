from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .media_object import MediaObject

if TYPE_CHECKING:
    MediaObject_Text_Ref = Union[MediaObject, Text, Ref]
else:
    MediaObject_Text_Ref = Union[Is["MediaObject"], Text, Ref]


class AudioObject(MediaObject):
    """An audio file."""
    schema_type: ClassVar[str] = "AudioObject"
    caption: MediaObject_Text_Ref | list[MediaObject_Text_Ref] | None = Field(default=None)
    embedded_text_caption: Text | list[Text] | None = Field(default=None, validation_alias="embeddedTextCaption", serialization_alias="embeddedTextCaption")
    transcript: Text | list[Text] | None = Field(default=None)
