from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .media_object import MediaObject

if TYPE_CHECKING:
    MediaObject_Ref = Union[MediaObject, Ref]
else:
    MediaObject_Ref = Union[Is["MediaObject"], Ref]


class MediaReviewItem(CreativeWork):
    """Represents an item or group of closely related items treated as a unit for the sake of evaluation in a [[MediaReview]]. Authorship etc. apply to the items rather than to the curation/grouping or reviewing party."""
    schema_type: ClassVar[str] = "MediaReviewItem"
    media_item_appearance: MediaObject_Ref | list[MediaObject_Ref] | None = Field(default=None, validation_alias="mediaItemAppearance", serialization_alias="mediaItemAppearance")
