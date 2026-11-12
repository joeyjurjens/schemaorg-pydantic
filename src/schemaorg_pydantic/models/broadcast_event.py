from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Ref, Text
from .publication_event import PublicationEvent

if TYPE_CHECKING:
    from .event import Event
    from .language import Language

if TYPE_CHECKING:
    Event_Ref = Union[Event, Ref]
else:
    Event_Ref = Union[Is["Event"], Ref]

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]


class BroadcastEvent(PublicationEvent):
    """An over the air or online broadcast event."""
    schema_type: ClassVar[str] = "BroadcastEvent"
    broadcast_of_event: Event_Ref | list[Event_Ref] | None = Field(default=None, validation_alias="broadcastOfEvent", serialization_alias="broadcastOfEvent")
    is_live_broadcast: Boolean | list[Boolean] | None = Field(default=None, validation_alias="isLiveBroadcast", serialization_alias="isLiveBroadcast")
    subtitle_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="subtitleLanguage", serialization_alias="subtitleLanguage")
    video_format: Text | list[Text] | None = Field(default=None, validation_alias="videoFormat", serialization_alias="videoFormat")
