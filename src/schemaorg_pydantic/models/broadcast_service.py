from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .service import Service

if TYPE_CHECKING:
    from .broadcast_channel import BroadcastChannel
    from .broadcast_frequency_specification import BroadcastFrequencySpecification
    from .language import Language
    from .organization import Organization

if TYPE_CHECKING:
    BroadcastChannel_Ref = Union[BroadcastChannel, Ref]
else:
    BroadcastChannel_Ref = Union[Is["BroadcastChannel"], Ref]

if TYPE_CHECKING:
    BroadcastFrequencySpecification_Text_Ref = Union[BroadcastFrequencySpecification, Text, Ref]
else:
    BroadcastFrequencySpecification_Text_Ref = Union[Is["BroadcastFrequencySpecification"], Text, Ref]

if TYPE_CHECKING:
    BroadcastService_Ref = Union["BroadcastService", Ref]
else:
    BroadcastService_Ref = Union[Is["BroadcastService"], Ref]

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]


class BroadcastService(Service):
    """A delivery service through which content is provided via broadcast over the air or online."""
    schema_type: ClassVar[str] = "BroadcastService"
    broadcast_affiliate_of: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="broadcastAffiliateOf", serialization_alias="broadcastAffiliateOf")
    broadcast_display_name: Text | list[Text] | None = Field(default=None, validation_alias="broadcastDisplayName", serialization_alias="broadcastDisplayName")
    broadcast_frequency: BroadcastFrequencySpecification_Text_Ref | list[BroadcastFrequencySpecification_Text_Ref] | None = Field(default=None, validation_alias="broadcastFrequency", serialization_alias="broadcastFrequency")
    broadcast_timezone: Text | list[Text] | None = Field(default=None, validation_alias="broadcastTimezone", serialization_alias="broadcastTimezone")
    broadcaster: Organization_Ref | list[Organization_Ref] | None = Field(default=None)
    call_sign: Text | list[Text] | None = Field(default=None, validation_alias="callSign", serialization_alias="callSign")
    has_broadcast_channel: BroadcastChannel_Ref | list[BroadcastChannel_Ref] | None = Field(default=None, validation_alias="hasBroadcastChannel", serialization_alias="hasBroadcastChannel")
    in_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="inLanguage", serialization_alias="inLanguage")
    parent_service: BroadcastService_Ref | list[BroadcastService_Ref] | None = Field(default=None, validation_alias="parentService", serialization_alias="parentService")
    video_format: Text | list[Text] | None = Field(default=None, validation_alias="videoFormat", serialization_alias="videoFormat")
