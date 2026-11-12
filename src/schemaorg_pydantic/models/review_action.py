from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .assess_action import AssessAction

if TYPE_CHECKING:
    from .review import Review

if TYPE_CHECKING:
    Review_Ref = Union[Review, Ref]
else:
    Review_Ref = Union[Is["Review"], Ref]


class ReviewAction(AssessAction):
    """The act of producing a balanced opinion about the object for an audience. An agent reviews an object with participants resulting in a review."""
    schema_type: ClassVar[str] = "ReviewAction"
    result_review: Review_Ref | list[Review_Ref] | None = Field(default=None, validation_alias="resultReview", serialization_alias="resultReview")
