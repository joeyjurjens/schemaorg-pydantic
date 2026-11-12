from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Number, Ref, Text
from .financial_product import FinancialProduct

if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount
    from .quantitative_value import QuantitativeValue
    from .repayment_specification import RepaymentSpecification
    from .thing import Thing

if TYPE_CHECKING:
    MonetaryAmount_Number_Ref = Union[MonetaryAmount, Number, Ref]
else:
    MonetaryAmount_Number_Ref = Union[Is["MonetaryAmount"], Number, Ref]

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]

if TYPE_CHECKING:
    RepaymentSpecification_Ref = Union[RepaymentSpecification, Ref]
else:
    RepaymentSpecification_Ref = Union[Is["RepaymentSpecification"], Ref]

if TYPE_CHECKING:
    Thing_Text_Ref = Union[Thing, Text, Ref]
else:
    Thing_Text_Ref = Union[Is["Thing"], Text, Ref]


class LoanOrCredit(FinancialProduct):
    """A financial product for the loaning of an amount of money, or line of credit, under agreed terms and charges."""
    schema_type: ClassVar[str] = "LoanOrCredit"
    amount: MonetaryAmount_Number_Ref | list[MonetaryAmount_Number_Ref] | None = Field(default=None)
    currency: Text | list[Text] | None = Field(default=None)
    grace_period: Text | list[Text] | None = Field(default=None, validation_alias="gracePeriod", serialization_alias="gracePeriod")
    loan_repayment_form: RepaymentSpecification_Ref | list[RepaymentSpecification_Ref] | None = Field(default=None, validation_alias="loanRepaymentForm", serialization_alias="loanRepaymentForm")
    loan_term: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="loanTerm", serialization_alias="loanTerm")
    loan_type: Text | list[Text] | None = Field(default=None, validation_alias="loanType", serialization_alias="loanType")
    recourse_loan: Boolean | list[Boolean] | None = Field(default=None, validation_alias="recourseLoan", serialization_alias="recourseLoan")
    renegotiable_loan: Boolean | list[Boolean] | None = Field(default=None, validation_alias="renegotiableLoan", serialization_alias="renegotiableLoan")
    required_collateral: Thing_Text_Ref | list[Thing_Text_Ref] | None = Field(default=None, validation_alias="requiredCollateral", serialization_alias="requiredCollateral")
