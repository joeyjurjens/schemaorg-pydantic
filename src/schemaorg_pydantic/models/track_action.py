from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .find_action import FindAction
from .delivery_method import DeliveryMethod


class TrackAction(FindAction):
    """An agent tracks an object for updates."""
    schema_type: ClassVar[str] = "TrackAction"
    delivery_method: DeliveryMethod | list[DeliveryMethod] | None = Field(default=None, validation_alias="deliveryMethod", serialization_alias="deliveryMethod")
