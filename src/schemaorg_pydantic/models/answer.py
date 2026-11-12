from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .comment import Comment

if TYPE_CHECKING:
    from .web_content import WebContent

if TYPE_CHECKING:
    Comment_WebContent_Ref = Union[Comment, WebContent, Ref]
else:
    Comment_WebContent_Ref = Union[Is["Comment"], Is["WebContent"], Ref]


class Answer(Comment):
    """An answer offered to a question; perhaps correct, perhaps opinionated or wrong."""
    schema_type: ClassVar[str] = "Answer"
    answer_explanation: Comment_WebContent_Ref | list[Comment_WebContent_Ref] | None = Field(default=None, validation_alias="answerExplanation", serialization_alias="answerExplanation")
