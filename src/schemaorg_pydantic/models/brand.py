from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text, Url
from .intangible import Intangible

if TYPE_CHECKING:
    from .aggregate_rating import AggregateRating
    from .image_object import ImageObject
    from .review import Review

if TYPE_CHECKING:
    AggregateRating_Ref = Union[AggregateRating, Ref]
else:
    AggregateRating_Ref = Union[Is["AggregateRating"], Ref]

if TYPE_CHECKING:
    ImageObject_Url_Ref = Union[ImageObject, Url, Ref]
else:
    ImageObject_Url_Ref = Union[Is["ImageObject"], Url, Ref]

if TYPE_CHECKING:
    Review_Ref = Union[Review, Ref]
else:
    Review_Ref = Union[Is["Review"], Ref]


class Brand(Intangible):
    """A brand is a name used by an organization or business person for labeling a product, product group, or similar."""
    schema_type: ClassVar[str] = "Brand"
    aggregate_rating: AggregateRating_Ref | list[AggregateRating_Ref] | None = Field(default=None, validation_alias="aggregateRating", serialization_alias="aggregateRating")
    logo: ImageObject_Url_Ref | list[ImageObject_Url_Ref] | None = Field(default=None)
    review: Review_Ref | list[Review_Ref] | None = Field(default=None)
    slogan: Text | list[Text] | None = Field(default=None)
