from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Ref, Text
from .media_object import MediaObject

if TYPE_CHECKING:
    from .property_value import PropertyValue

if TYPE_CHECKING:
    MediaObject_Text_Ref = Union[MediaObject, Text, Ref]
else:
    MediaObject_Text_Ref = Union[Is["MediaObject"], Text, Ref]

if TYPE_CHECKING:
    PropertyValue_Text_Ref = Union[PropertyValue, Text, Ref]
else:
    PropertyValue_Text_Ref = Union[Is["PropertyValue"], Text, Ref]


class ImageObject(MediaObject):
    """An image file."""
    schema_type: ClassVar[str] = "ImageObject"
    caption: MediaObject_Text_Ref | list[MediaObject_Text_Ref] | None = Field(default=None)
    embedded_text_caption: Text | list[Text] | None = Field(default=None, validation_alias="embeddedTextCaption", serialization_alias="embeddedTextCaption")
    exif_data: PropertyValue_Text_Ref | list[PropertyValue_Text_Ref] | None = Field(default=None, validation_alias="exifData", serialization_alias="exifData")
    representative_of_page: Boolean | list[Boolean] | None = Field(default=None, validation_alias="representativeOfPage", serialization_alias="representativeOfPage")
