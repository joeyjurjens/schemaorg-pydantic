from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .intangible import Intangible
from .payment_method_type import PaymentMethodType


class PaymentMethod(Intangible):
    """A payment method is a standardized procedure for transferring the monetary amount for a purchase. Payment methods are characterized by the legal and technical structures used, and by the organization or group carrying out the transaction. The following legacy values should be accepted:"""
    schema_type: ClassVar[str] = "PaymentMethod"
    payment_method_type: PaymentMethodType | list[PaymentMethodType] | None = Field(default=None, validation_alias="paymentMethodType", serialization_alias="paymentMethodType")
