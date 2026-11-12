from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .intangible import Intangible

if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person
    from .structured_value import StructuredValue

Number_Text = Union[Number, Text]
if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    StructuredValue_Text_Ref = Union[StructuredValue, Text, Ref]
else:
    StructuredValue_Text_Ref = Union[Is["StructuredValue"], Text, Ref]


class Rating(Intangible):
    """A rating is an evaluation on a numeric scale, such as 1 to 5 stars."""
    schema_type: ClassVar[str] = "Rating"
    author: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    best_rating: Number_Text | list[Number_Text] | None = Field(default=None, validation_alias="bestRating", serialization_alias="bestRating")
    rating_explanation: Text | list[Text] | None = Field(default=None, validation_alias="ratingExplanation", serialization_alias="ratingExplanation")
    rating_value: Number_Text | list[Number_Text] | None = Field(default=None, validation_alias="ratingValue", serialization_alias="ratingValue")
    review_aspect: StructuredValue_Text_Ref | list[StructuredValue_Text_Ref] | None = Field(default=None, validation_alias="reviewAspect", serialization_alias="reviewAspect")
    worst_rating: Number_Text | list[Number_Text] | None = Field(default=None, validation_alias="worstRating", serialization_alias="worstRating")
