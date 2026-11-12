from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .update_action import UpdateAction

if TYPE_CHECKING:
    from .thing import Thing

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]


class ReplaceAction(UpdateAction):
    """The act of editing a recipient by replacing an old object with a new object."""
    schema_type: ClassVar[str] = "ReplaceAction"
    replacee: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    replacer: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
