from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .interact_action import InteractAction

if TYPE_CHECKING:
    from .event import Event

if TYPE_CHECKING:
    Event_Ref = Union[Event, Ref]
else:
    Event_Ref = Union[Is["Event"], Ref]


class JoinAction(InteractAction):
    """An agent joins an event/group with participants/friends at a location."""
    schema_type: ClassVar[str] = "JoinAction"
    event: Event_Ref | list[Event_Ref] | None = Field(default=None)
