from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text, Url
from .review import Review
from .media_manipulation_rating_enumeration import MediaManipulationRatingEnumeration

if TYPE_CHECKING:
    from .media_object import MediaObject
    from .web_page import WebPage

if TYPE_CHECKING:
    MediaObject_WebPage_Url_Ref = Union[MediaObject, WebPage, Url, Ref]
else:
    MediaObject_WebPage_Url_Ref = Union[Is["MediaObject"], Is["WebPage"], Url, Ref]


class MediaReview(Review):
    """A [[MediaReview]] is a more specialized form of Review dedicated to the evaluation of media content online, typically in the context of fact-checking and misinformation.\n    For more general reviews of media in the broader sense, use [[UserReview]], [[CriticReview]] or other [[Review]] types. This definition is\n    a work in progress. While the [[MediaManipulationRatingEnumeration]] list reflects significant community review amongst fact-checkers and others working\n    to combat misinformation, the specific structures for representing media objects, their versions and publication context, are still evolving. Similarly, best practices for the relationship between [[MediaReview]] and [[ClaimReview]] markup have not yet been finalized."""
    schema_type: ClassVar[str] = "MediaReview"
    media_authenticity_category: MediaManipulationRatingEnumeration | list[MediaManipulationRatingEnumeration] | None = Field(default=None, validation_alias="mediaAuthenticityCategory", serialization_alias="mediaAuthenticityCategory")
    original_media_context_description: Text | list[Text] | None = Field(default=None, validation_alias="originalMediaContextDescription", serialization_alias="originalMediaContextDescription")
    original_media_link: MediaObject_WebPage_Url_Ref | list[MediaObject_WebPage_Url_Ref] | None = Field(default=None, validation_alias="originalMediaLink", serialization_alias="originalMediaLink")
