from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .event import Event

if TYPE_CHECKING:
    from .broadcast_service import BroadcastService
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    BroadcastService_Ref = Union[BroadcastService, Ref]
else:
    BroadcastService_Ref = Union[Is["BroadcastService"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]


class PublicationEvent(Event):
    """A PublicationEvent corresponds indifferently to the event of publication for a CreativeWork of any type, e.g. a broadcast event, an on-demand event, a book/journal publication via a variety of delivery media."""
    schema_type: ClassVar[str] = "PublicationEvent"
    published_by: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="publishedBy", serialization_alias="publishedBy")
    published_on: BroadcastService_Ref | list[BroadcastService_Ref] | None = Field(default=None, validation_alias="publishedOn", serialization_alias="publishedOn")
