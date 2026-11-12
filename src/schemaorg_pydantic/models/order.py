from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Date, DateTime, Is, Number, Ref, Text, Url
from .intangible import Intangible
from .order_status import OrderStatus

if TYPE_CHECKING:
    from .invoice import Invoice
    from .offer import Offer
    from .order_item import OrderItem
    from .organization import Organization
    from .parcel_delivery import ParcelDelivery
    from .payment_method import PaymentMethod
    from .person import Person
    from .postal_address import PostalAddress
    from .product import Product
    from .service import Service

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    Invoice_Ref = Union[Invoice, Ref]
else:
    Invoice_Ref = Union[Is["Invoice"], Ref]

Number_Text = Union[Number, Text]
if TYPE_CHECKING:
    Offer_Ref = Union[Offer, Ref]
else:
    Offer_Ref = Union[Is["Offer"], Ref]

if TYPE_CHECKING:
    OrderItem_Product_Service_Ref = Union[OrderItem, Product, Service, Ref]
else:
    OrderItem_Product_Service_Ref = Union[Is["OrderItem"], Is["Product"], Is["Service"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    ParcelDelivery_Ref = Union[ParcelDelivery, Ref]
else:
    ParcelDelivery_Ref = Union[Is["ParcelDelivery"], Ref]

if TYPE_CHECKING:
    PaymentMethod_Text_Ref = Union[PaymentMethod, Text, Ref]
else:
    PaymentMethod_Text_Ref = Union[Is["PaymentMethod"], Text, Ref]

if TYPE_CHECKING:
    PostalAddress_Ref = Union[PostalAddress, Ref]
else:
    PostalAddress_Ref = Union[Is["PostalAddress"], Ref]


class Order(Intangible):
    """An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer."""
    schema_type: ClassVar[str] = "Order"
    accepted_offer: Offer_Ref | list[Offer_Ref] | None = Field(default=None, validation_alias="acceptedOffer", serialization_alias="acceptedOffer")
    billing_address: PostalAddress_Ref | list[PostalAddress_Ref] | None = Field(default=None, validation_alias="billingAddress", serialization_alias="billingAddress")
    broker: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    confirmation_number: Text | list[Text] | None = Field(default=None, validation_alias="confirmationNumber", serialization_alias="confirmationNumber")
    customer: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    discount: Number_Text | list[Number_Text] | None = Field(default=None)
    discount_code: Text | list[Text] | None = Field(default=None, validation_alias="discountCode", serialization_alias="discountCode")
    discount_currency: Text | list[Text] | None = Field(default=None, validation_alias="discountCurrency", serialization_alias="discountCurrency")
    is_gift: Boolean | list[Boolean] | None = Field(default=None, validation_alias="isGift", serialization_alias="isGift")
    order_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="orderDate", serialization_alias="orderDate")
    order_delivery: ParcelDelivery_Ref | list[ParcelDelivery_Ref] | None = Field(default=None, validation_alias="orderDelivery", serialization_alias="orderDelivery")
    order_number: Text | list[Text] | None = Field(default=None, validation_alias="orderNumber", serialization_alias="orderNumber")
    order_status: OrderStatus | list[OrderStatus] | None = Field(default=None, validation_alias="orderStatus", serialization_alias="orderStatus")
    ordered_item: OrderItem_Product_Service_Ref | list[OrderItem_Product_Service_Ref] | None = Field(default=None, validation_alias="orderedItem", serialization_alias="orderedItem")
    part_of_invoice: Invoice_Ref | list[Invoice_Ref] | None = Field(default=None, validation_alias="partOfInvoice", serialization_alias="partOfInvoice")
    payment_due_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="paymentDueDate", serialization_alias="paymentDueDate")
    payment_method: PaymentMethod_Text_Ref | list[PaymentMethod_Text_Ref] | None = Field(default=None, validation_alias="paymentMethod", serialization_alias="paymentMethod")
    payment_method_id: Text | list[Text] | None = Field(default=None, validation_alias="paymentMethodId", serialization_alias="paymentMethodId")
    payment_url: Url | list[Url] | None = Field(default=None, validation_alias="paymentUrl", serialization_alias="paymentUrl")
    seller: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
