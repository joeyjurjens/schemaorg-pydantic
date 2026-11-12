from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .action import Action

if TYPE_CHECKING:
    from .audience import Audience
    from .event import Event

if TYPE_CHECKING:
    Audience_Ref = Union[Audience, Ref]
else:
    Audience_Ref = Union[Is["Audience"], Ref]

if TYPE_CHECKING:
    Event_Ref = Union[Event, Ref]
else:
    Event_Ref = Union[Is["Event"], Ref]


class PlayAction(Action):
    """The act of playing/exercising/training/performing for enjoyment, leisure, recreation, competition or exercise."""
    schema_type: ClassVar[str] = "PlayAction"
    audience: Audience_Ref | list[Audience_Ref] | None = Field(default=None)
    event: Event_Ref | list[Event_Ref] | None = Field(default=None)
