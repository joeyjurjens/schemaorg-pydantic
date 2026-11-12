from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .assess_action import AssessAction

if TYPE_CHECKING:
    from .thing import Thing

if TYPE_CHECKING:
    Thing_Text_Ref = Union[Thing, Text, Ref]
else:
    Thing_Text_Ref = Union[Is["Thing"], Text, Ref]


class ChooseAction(AssessAction):
    """The act of expressing a preference from a set of options or a large or unbounded set of choices/options."""
    schema_type: ClassVar[str] = "ChooseAction"
    action_option: Thing_Text_Ref | list[Thing_Text_Ref] | None = Field(default=None, validation_alias="actionOption", serialization_alias="actionOption")
