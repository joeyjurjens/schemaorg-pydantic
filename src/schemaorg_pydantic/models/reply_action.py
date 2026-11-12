from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .communicate_action import CommunicateAction

if TYPE_CHECKING:
    from .comment import Comment

if TYPE_CHECKING:
    Comment_Ref = Union[Comment, Ref]
else:
    Comment_Ref = Union[Is["Comment"], Ref]


class ReplyAction(CommunicateAction):
    """The act of responding to a question/message asked/sent by the object. Related to [[AskAction]]."""
    schema_type: ClassVar[str] = "ReplyAction"
    result_comment: Comment_Ref | list[Comment_Ref] | None = Field(default=None, validation_alias="resultComment", serialization_alias="resultComment")
