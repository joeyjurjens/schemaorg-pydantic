from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .solve_math_action import SolveMathAction

if TYPE_CHECKING:
    SolveMathAction_Text_Ref = Union[SolveMathAction, Text, Ref]
else:
    SolveMathAction_Text_Ref = Union[Is["SolveMathAction"], Text, Ref]


class MathSolver(CreativeWork):
    """A math solver which is capable of solving a subset of mathematical problems."""
    schema_type: ClassVar[str] = "MathSolver"
    math_expression: SolveMathAction_Text_Ref | list[SolveMathAction_Text_Ref] | None = Field(default=None, validation_alias="mathExpression", serialization_alias="mathExpression")
