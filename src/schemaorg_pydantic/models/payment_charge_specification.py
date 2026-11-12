from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .price_specification import PriceSpecification
from .delivery_method import DeliveryMethod

if TYPE_CHECKING:
    from .payment_method import PaymentMethod

if TYPE_CHECKING:
    PaymentMethod_Ref = Union[PaymentMethod, Ref]
else:
    PaymentMethod_Ref = Union[Is["PaymentMethod"], Ref]


class PaymentChargeSpecification(PriceSpecification):
    """The costs of settling the payment using a particular payment method."""
    schema_type: ClassVar[str] = "PaymentChargeSpecification"
    applies_to_delivery_method: DeliveryMethod | list[DeliveryMethod] | None = Field(default=None, validation_alias="appliesToDeliveryMethod", serialization_alias="appliesToDeliveryMethod")
    applies_to_payment_method: PaymentMethod_Ref | list[PaymentMethod_Ref] | None = Field(default=None, validation_alias="appliesToPaymentMethod", serialization_alias="appliesToPaymentMethod")
