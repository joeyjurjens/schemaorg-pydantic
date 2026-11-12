from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref, Text
from .comment import Comment

if TYPE_CHECKING:
    from .answer import Answer
    from .item_list import ItemList

if TYPE_CHECKING:
    Answer_ItemList_Ref = Union[Answer, ItemList, Ref]
else:
    Answer_ItemList_Ref = Union[Is["Answer"], Is["ItemList"], Ref]


class Question(Comment):
    """A specific question - e.g. from a user seeking answers online, or collected in a Frequently Asked Questions (FAQ) document."""
    schema_type: ClassVar[str] = "Question"
    accepted_answer: Answer_ItemList_Ref | list[Answer_ItemList_Ref] | None = Field(default=None, validation_alias="acceptedAnswer", serialization_alias="acceptedAnswer")
    answer_count: Integer | list[Integer] | None = Field(default=None, validation_alias="answerCount", serialization_alias="answerCount")
    edu_question_type: Text | list[Text] | None = Field(default=None, validation_alias="eduQuestionType", serialization_alias="eduQuestionType")
    suggested_answer: Answer_ItemList_Ref | list[Answer_ItemList_Ref] | None = Field(default=None, validation_alias="suggestedAnswer", serialization_alias="suggestedAnswer")
