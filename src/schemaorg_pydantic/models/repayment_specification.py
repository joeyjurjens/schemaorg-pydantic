from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

if TYPE_CHECKING:
    MonetaryAmount_Number_Ref = Union[MonetaryAmount, Number, Ref]
else:
    MonetaryAmount_Number_Ref = Union[Is["MonetaryAmount"], Number, Ref]

if TYPE_CHECKING:
    MonetaryAmount_Ref = Union[MonetaryAmount, Ref]
else:
    MonetaryAmount_Ref = Union[Is["MonetaryAmount"], Ref]


class RepaymentSpecification(StructuredValue):
    """A structured value representing repayment."""
    schema_type: ClassVar[str] = "RepaymentSpecification"
    down_payment: MonetaryAmount_Number_Ref | list[MonetaryAmount_Number_Ref] | None = Field(default=None, validation_alias="downPayment", serialization_alias="downPayment")
    early_prepayment_penalty: MonetaryAmount_Ref | list[MonetaryAmount_Ref] | None = Field(default=None, validation_alias="earlyPrepaymentPenalty", serialization_alias="earlyPrepaymentPenalty")
    loan_payment_amount: MonetaryAmount_Ref | list[MonetaryAmount_Ref] | None = Field(default=None, validation_alias="loanPaymentAmount", serialization_alias="loanPaymentAmount")
    loan_payment_frequency: Number | list[Number] | None = Field(default=None, validation_alias="loanPaymentFrequency", serialization_alias="loanPaymentFrequency")
    number_of_loan_payments: Number | list[Number] | None = Field(default=None, validation_alias="numberOfLoanPayments", serialization_alias="numberOfLoanPayments")
