from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Is, Ref
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .audience import Audience
    from .contact_point import ContactPoint
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    R5c65ac19 = Union[Audience, ContactPoint, Organization, Person, Ref]
else:
    R5c65ac19 = Union[Is["Audience"], Is["ContactPoint"], Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Audience_Organization_Person_Ref = Union[Audience, Organization, Person, Ref]
else:
    Audience_Organization_Person_Ref = Union[Is["Audience"], Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    ContactPoint_Organization_Person_Ref = Union[ContactPoint, Organization, Person, Ref]
else:
    ContactPoint_Organization_Person_Ref = Union[Is["ContactPoint"], Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    CreativeWork_Ref = Union[CreativeWork, Ref]
else:
    CreativeWork_Ref = Union[Is["CreativeWork"], Ref]

Date_DateTime = Union[Date, DateTime]

class Message(CreativeWork):
    """A single message from a sender to one or more organizations or people."""
    schema_type: ClassVar[str] = "Message"
    bcc_recipient: ContactPoint_Organization_Person_Ref | list[ContactPoint_Organization_Person_Ref] | None = Field(default=None, validation_alias="bccRecipient", serialization_alias="bccRecipient")
    cc_recipient: ContactPoint_Organization_Person_Ref | list[ContactPoint_Organization_Person_Ref] | None = Field(default=None, validation_alias="ccRecipient", serialization_alias="ccRecipient")
    date_read: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="dateRead", serialization_alias="dateRead")
    date_received: DateTime | list[DateTime] | None = Field(default=None, validation_alias="dateReceived", serialization_alias="dateReceived")
    date_sent: DateTime | list[DateTime] | None = Field(default=None, validation_alias="dateSent", serialization_alias="dateSent")
    message_attachment: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="messageAttachment", serialization_alias="messageAttachment")
    recipient: R5c65ac19 | list[R5c65ac19] | None = Field(default=None)
    sender: Audience_Organization_Person_Ref | list[Audience_Organization_Person_Ref] | None = Field(default=None)
    to_recipient: R5c65ac19 | list[R5c65ac19] | None = Field(default=None, validation_alias="toRecipient", serialization_alias="toRecipient")
