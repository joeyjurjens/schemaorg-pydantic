from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .action import Action


class SolveMathAction(Action):
    """The action that takes in a math expression and directs users to a page potentially capable of solving/simplifying that expression."""
    schema_type: ClassVar[str] = "SolveMathAction"
    edu_question_type: Text | list[Text] | None = Field(default=None, validation_alias="eduQuestionType", serialization_alias="eduQuestionType")
