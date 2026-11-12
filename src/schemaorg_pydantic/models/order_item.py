from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .structured_value import StructuredValue
from .order_status import OrderStatus

if TYPE_CHECKING:
    from .parcel_delivery import ParcelDelivery
    from .product import Product
    from .quantitative_value import QuantitativeValue
    from .service import Service

if TYPE_CHECKING:
    OrderItem_Product_Service_Ref = Union["OrderItem", Product, Service, Ref]
else:
    OrderItem_Product_Service_Ref = Union[Is["OrderItem"], Is["Product"], Is["Service"], Ref]

if TYPE_CHECKING:
    ParcelDelivery_Ref = Union[ParcelDelivery, Ref]
else:
    ParcelDelivery_Ref = Union[Is["ParcelDelivery"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Number_Ref = Union[QuantitativeValue, Number, Ref]
else:
    QuantitativeValue_Number_Ref = Union[Is["QuantitativeValue"], Number, Ref]


class OrderItem(StructuredValue):
    """An order item is a line of an order. It includes the quantity and shipping details of a bought offer."""
    schema_type: ClassVar[str] = "OrderItem"
    order_delivery: ParcelDelivery_Ref | list[ParcelDelivery_Ref] | None = Field(default=None, validation_alias="orderDelivery", serialization_alias="orderDelivery")
    order_item_number: Text | list[Text] | None = Field(default=None, validation_alias="orderItemNumber", serialization_alias="orderItemNumber")
    order_item_status: OrderStatus | list[OrderStatus] | None = Field(default=None, validation_alias="orderItemStatus", serialization_alias="orderItemStatus")
    order_quantity: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="orderQuantity", serialization_alias="orderQuantity")
    ordered_item: OrderItem_Product_Service_Ref | list[OrderItem_Product_Service_Ref] | None = Field(default=None, validation_alias="orderedItem", serialization_alias="orderedItem")
