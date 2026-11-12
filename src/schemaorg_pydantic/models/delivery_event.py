from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import DateTime, Text
from .event import Event
from .delivery_method import DeliveryMethod


class DeliveryEvent(Event):
    """An event involving the delivery of an item."""
    schema_type: ClassVar[str] = "DeliveryEvent"
    access_code: Text | list[Text] | None = Field(default=None, validation_alias="accessCode", serialization_alias="accessCode")
    available_from: DateTime | list[DateTime] | None = Field(default=None, validation_alias="availableFrom", serialization_alias="availableFrom")
    available_through: DateTime | list[DateTime] | None = Field(default=None, validation_alias="availableThrough", serialization_alias="availableThrough")
    has_delivery_method: DeliveryMethod | list[DeliveryMethod] | None = Field(default=None, validation_alias="hasDeliveryMethod", serialization_alias="hasDeliveryMethod")
