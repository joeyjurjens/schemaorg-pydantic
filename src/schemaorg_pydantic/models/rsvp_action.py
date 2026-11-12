from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref
from .inform_action import InformAction
from .rsvp_response_type import RsvpResponseType

if TYPE_CHECKING:
    from .comment import Comment

if TYPE_CHECKING:
    Comment_Ref = Union[Comment, Ref]
else:
    Comment_Ref = Union[Is["Comment"], Ref]


class RsvpAction(InformAction):
    """The act of notifying an event organizer as to whether you expect to attend the event."""
    schema_type: ClassVar[str] = "RsvpAction"
    additional_number_of_guests: Number | list[Number] | None = Field(default=None, validation_alias="additionalNumberOfGuests", serialization_alias="additionalNumberOfGuests")
    comment: Comment_Ref | list[Comment_Ref] | None = Field(default=None)
    rsvp_response: RsvpResponseType | list[RsvpResponseType] | None = Field(default=None, validation_alias="rsvpResponse", serialization_alias="rsvpResponse")
