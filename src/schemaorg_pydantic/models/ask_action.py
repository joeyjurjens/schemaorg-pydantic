from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .communicate_action import CommunicateAction

if TYPE_CHECKING:
    from .question import Question

if TYPE_CHECKING:
    Question_Ref = Union[Question, Ref]
else:
    Question_Ref = Union[Is["Question"], Ref]


class AskAction(CommunicateAction):
    """The act of posing a question / favor to someone."""
    schema_type: ClassVar[str] = "AskAction"
    question: Question_Ref | list[Question_Ref] | None = Field(default=None)
