from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Number, Ref
from .financial_product import FinancialProduct
from .payment_method import PaymentMethod

if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

Boolean_Number = Union[Boolean, Number]
if TYPE_CHECKING:
    MonetaryAmount_Number_Ref = Union[MonetaryAmount, Number, Ref]
else:
    MonetaryAmount_Number_Ref = Union[Is["MonetaryAmount"], Number, Ref]

if TYPE_CHECKING:
    MonetaryAmount_Ref = Union[MonetaryAmount, Ref]
else:
    MonetaryAmount_Ref = Union[Is["MonetaryAmount"], Ref]


class PaymentCard(FinancialProduct, PaymentMethod):
    """A payment method using a credit, debit, store or other card to associate the payment with an account."""
    schema_type: ClassVar[str] = "PaymentCard"
    cash_back: Boolean_Number | list[Boolean_Number] | None = Field(default=None, validation_alias="cashBack", serialization_alias="cashBack")
    contactless_payment: Boolean | list[Boolean] | None = Field(default=None, validation_alias="contactlessPayment", serialization_alias="contactlessPayment")
    floor_limit: MonetaryAmount_Ref | list[MonetaryAmount_Ref] | None = Field(default=None, validation_alias="floorLimit", serialization_alias="floorLimit")
    monthly_minimum_repayment_amount: MonetaryAmount_Number_Ref | list[MonetaryAmount_Number_Ref] | None = Field(default=None, validation_alias="monthlyMinimumRepaymentAmount", serialization_alias="monthlyMinimumRepaymentAmount")
