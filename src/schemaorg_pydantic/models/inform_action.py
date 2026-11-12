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


class InformAction(CommunicateAction):
    """The act of notifying someone of information pertinent to them, with no expectation of a response."""
    schema_type: ClassVar[str] = "InformAction"
    event: Event_Ref | list[Event_Ref] | None = Field(default=None)
