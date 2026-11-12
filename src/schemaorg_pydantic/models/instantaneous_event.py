from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import DateTime, Is, Ref
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .thing import Thing

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]


class InstantaneousEvent(StructuredValue):
    """An event with no duration, like for instance a computer log entry."""
    schema_type: ClassVar[str] = "InstantaneousEvent"
    data: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    source: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    timestamp: DateTime | list[DateTime] | None = Field(default=None)
