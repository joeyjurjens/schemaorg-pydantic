from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .item_list import ItemList
    from .list_item import ListItem
    from .rating import Rating
    from .structured_value import StructuredValue
    from .thing import Thing
    from .web_content import WebContent

if TYPE_CHECKING:
    R318be025 = Union[ItemList, ListItem, WebContent, Text, Ref]
else:
    R318be025 = Union[Is["ItemList"], Is["ListItem"], Is["WebContent"], Text, Ref]

if TYPE_CHECKING:
    Rating_Ref = Union[Rating, Ref]
else:
    Rating_Ref = Union[Is["Rating"], Ref]

if TYPE_CHECKING:
    Review_Ref = Union["Review", Ref]
else:
    Review_Ref = Union[Is["Review"], Ref]

if TYPE_CHECKING:
    StructuredValue_Text_Ref = Union[StructuredValue, Text, Ref]
else:
    StructuredValue_Text_Ref = Union[Is["StructuredValue"], Text, Ref]

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]


class Review(CreativeWork):
    """A review of an item - for example, of a restaurant, movie, or store."""
    schema_type: ClassVar[str] = "Review"
    associated_claim_review: Review_Ref | list[Review_Ref] | None = Field(default=None, validation_alias="associatedClaimReview", serialization_alias="associatedClaimReview")
    associated_media_review: Review_Ref | list[Review_Ref] | None = Field(default=None, validation_alias="associatedMediaReview", serialization_alias="associatedMediaReview")
    associated_review: Review_Ref | list[Review_Ref] | None = Field(default=None, validation_alias="associatedReview", serialization_alias="associatedReview")
    item_reviewed: Thing_Ref | list[Thing_Ref] | None = Field(default=None, validation_alias="itemReviewed", serialization_alias="itemReviewed")
    negative_notes: R318be025 | list[R318be025] | None = Field(default=None, validation_alias="negativeNotes", serialization_alias="negativeNotes")
    positive_notes: R318be025 | list[R318be025] | None = Field(default=None, validation_alias="positiveNotes", serialization_alias="positiveNotes")
    review_aspect: StructuredValue_Text_Ref | list[StructuredValue_Text_Ref] | None = Field(default=None, validation_alias="reviewAspect", serialization_alias="reviewAspect")
    review_body: Text | list[Text] | None = Field(default=None, validation_alias="reviewBody", serialization_alias="reviewBody")
    review_rating: Rating_Ref | list[Rating_Ref] | None = Field(default=None, validation_alias="reviewRating", serialization_alias="reviewRating")
