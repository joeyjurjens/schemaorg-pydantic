from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import DateTime, Is, Ref, Text, Time, Url
from .thing import Thing
from .action_status_type import ActionStatusType

if TYPE_CHECKING:
    from .entry_point import EntryPoint
    from .how_to import HowTo
    from .organization import Organization
    from .person import Person
    from .place import Place
    from .postal_address import PostalAddress
    from .virtual_location import VirtualLocation

DateTime_Time = Union[DateTime, Time]
if TYPE_CHECKING:
    EntryPoint_Url_Ref = Union[EntryPoint, Url, Ref]
else:
    EntryPoint_Url_Ref = Union[Is["EntryPoint"], Url, Ref]

if TYPE_CHECKING:
    HowTo_Ref = Union[HowTo, Ref]
else:
    HowTo_Ref = Union[Is["HowTo"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    R2967d0a9 = Union[Place, PostalAddress, VirtualLocation, Text, Ref]
else:
    R2967d0a9 = Union[Is["Place"], Is["PostalAddress"], Is["VirtualLocation"], Text, Ref]

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]


class Action(Thing):
    """An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role."""
    schema_type: ClassVar[str] = "Action"
    action_process: HowTo_Ref | list[HowTo_Ref] | None = Field(default=None, validation_alias="actionProcess", serialization_alias="actionProcess")
    action_status: ActionStatusType | list[ActionStatusType] | None = Field(default=None, validation_alias="actionStatus", serialization_alias="actionStatus")
    agent: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    end_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="endTime", serialization_alias="endTime")
    error: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    instrument: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    location: R2967d0a9 | list[R2967d0a9] | None = Field(default=None)
    object: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    participant: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    provider: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    result: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    start_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="startTime", serialization_alias="startTime")
    target: EntryPoint_Url_Ref | list[EntryPoint_Url_Ref] | None = Field(default=None)
