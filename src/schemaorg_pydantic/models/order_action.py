from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .trade_action import TradeAction
from .delivery_method import DeliveryMethod


class OrderAction(TradeAction):
    """An agent orders an object/product/service to be delivered/sent."""
    schema_type: ClassVar[str] = "OrderAction"
    delivery_method: DeliveryMethod | list[DeliveryMethod] | None = Field(default=None, validation_alias="deliveryMethod", serialization_alias="deliveryMethod")
