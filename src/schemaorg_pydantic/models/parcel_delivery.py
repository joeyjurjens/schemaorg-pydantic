from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Is, Ref, Text, Url
from .intangible import Intangible
from .delivery_method import DeliveryMethod

if TYPE_CHECKING:
    from .delivery_event import DeliveryEvent
    from .order import Order
    from .organization import Organization
    from .person import Person
    from .postal_address import PostalAddress
    from .product import Product

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    DeliveryEvent_Ref = Union[DeliveryEvent, Ref]
else:
    DeliveryEvent_Ref = Union[Is["DeliveryEvent"], Ref]

if TYPE_CHECKING:
    Order_Ref = Union[Order, Ref]
else:
    Order_Ref = Union[Is["Order"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    PostalAddress_Ref = Union[PostalAddress, Ref]
else:
    PostalAddress_Ref = Union[Is["PostalAddress"], Ref]

if TYPE_CHECKING:
    Product_Ref = Union[Product, Ref]
else:
    Product_Ref = Union[Is["Product"], Ref]


class ParcelDelivery(Intangible):
    """The delivery of a parcel either via the postal service or a commercial service."""
    schema_type: ClassVar[str] = "ParcelDelivery"
    delivery_address: PostalAddress_Ref | list[PostalAddress_Ref] | None = Field(default=None, validation_alias="deliveryAddress", serialization_alias="deliveryAddress")
    delivery_status: DeliveryEvent_Ref | list[DeliveryEvent_Ref] | None = Field(default=None, validation_alias="deliveryStatus", serialization_alias="deliveryStatus")
    expected_arrival_from: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="expectedArrivalFrom", serialization_alias="expectedArrivalFrom")
    expected_arrival_until: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="expectedArrivalUntil", serialization_alias="expectedArrivalUntil")
    has_delivery_method: DeliveryMethod | list[DeliveryMethod] | None = Field(default=None, validation_alias="hasDeliveryMethod", serialization_alias="hasDeliveryMethod")
    item_shipped: Product_Ref | list[Product_Ref] | None = Field(default=None, validation_alias="itemShipped", serialization_alias="itemShipped")
    origin_address: PostalAddress_Ref | list[PostalAddress_Ref] | None = Field(default=None, validation_alias="originAddress", serialization_alias="originAddress")
    part_of_order: Order_Ref | list[Order_Ref] | None = Field(default=None, validation_alias="partOfOrder", serialization_alias="partOfOrder")
    provider: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    tracking_number: Text | list[Text] | None = Field(default=None, validation_alias="trackingNumber", serialization_alias="trackingNumber")
    tracking_url: Url | list[Url] | None = Field(default=None, validation_alias="trackingUrl", serialization_alias="trackingUrl")
