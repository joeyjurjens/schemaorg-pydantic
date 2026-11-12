from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import DateTime, Integer, Is, Ref, Text, Time
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .action import Action
    from .place import Place
    from .postal_address import PostalAddress
    from .software_application import SoftwareApplication
    from .virtual_location import VirtualLocation
    from .web_site import WebSite

if TYPE_CHECKING:
    Action_Ref = Union[Action, Ref]
else:
    Action_Ref = Union[Is["Action"], Ref]

DateTime_Time = Union[DateTime, Time]
if TYPE_CHECKING:
    R2967d0a9 = Union[Place, PostalAddress, VirtualLocation, Text, Ref]
else:
    R2967d0a9 = Union[Is["Place"], Is["PostalAddress"], Is["VirtualLocation"], Text, Ref]

if TYPE_CHECKING:
    SoftwareApplication_WebSite_Ref = Union[SoftwareApplication, WebSite, Ref]
else:
    SoftwareApplication_WebSite_Ref = Union[Is["SoftwareApplication"], Is["WebSite"], Ref]


class InteractionCounter(StructuredValue):
    """A summary of how users have interacted with this CreativeWork. In most cases, authors will use a subtype to specify the specific type of interaction."""
    schema_type: ClassVar[str] = "InteractionCounter"
    end_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="endTime", serialization_alias="endTime")
    interaction_service: SoftwareApplication_WebSite_Ref | list[SoftwareApplication_WebSite_Ref] | None = Field(default=None, validation_alias="interactionService", serialization_alias="interactionService")
    interaction_type: Action_Ref | list[Action_Ref] | None = Field(default=None, validation_alias="interactionType", serialization_alias="interactionType")
    location: R2967d0a9 | list[R2967d0a9] | None = Field(default=None)
    start_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="startTime", serialization_alias="startTime")
    user_interaction_count: Integer | list[Integer] | None = Field(default=None, validation_alias="userInteractionCount", serialization_alias="userInteractionCount")
