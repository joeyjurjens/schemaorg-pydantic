from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .communicate_action import CommunicateAction

if TYPE_CHECKING:
    from .event import Event

if TYPE_CHECKING:
    Event_Ref = Union[Event, Ref]
else:
    Event_Ref = Union[Is["Event"], Ref]


class InviteAction(CommunicateAction):
    """The act of asking someone to attend an event. Reciprocal of RsvpAction."""
    schema_type: ClassVar[str] = "InviteAction"
    event: Event_Ref | list[Event_Ref] | None = Field(default=None)
