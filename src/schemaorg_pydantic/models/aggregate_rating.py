from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref
from .rating import Rating

if TYPE_CHECKING:
    from .thing import Thing

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]


class AggregateRating(Rating):
    """The average rating based on multiple ratings or reviews."""
    schema_type: ClassVar[str] = "AggregateRating"
    item_reviewed: Thing_Ref | list[Thing_Ref] | None = Field(default=None, validation_alias="itemReviewed", serialization_alias="itemReviewed")
    rating_count: Integer | list[Integer] | None = Field(default=None, validation_alias="ratingCount", serialization_alias="ratingCount")
    review_count: Integer | list[Integer] | None = Field(default=None, validation_alias="reviewCount", serialization_alias="reviewCount")
