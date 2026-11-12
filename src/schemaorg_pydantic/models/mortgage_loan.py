from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Ref
from .loan_or_credit import LoanOrCredit

if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

if TYPE_CHECKING:
    MonetaryAmount_Ref = Union[MonetaryAmount, Ref]
else:
    MonetaryAmount_Ref = Union[Is["MonetaryAmount"], Ref]


class MortgageLoan(LoanOrCredit):
    """A loan in which property or real estate is used as collateral. (A loan securitized against some real estate.)"""
    schema_type: ClassVar[str] = "MortgageLoan"
    domiciled_mortgage: Boolean | list[Boolean] | None = Field(default=None, validation_alias="domiciledMortgage", serialization_alias="domiciledMortgage")
    loan_mortgage_mandate_amount: MonetaryAmount_Ref | list[MonetaryAmount_Ref] | None = Field(default=None, validation_alias="loanMortgageMandateAmount", serialization_alias="loanMortgageMandateAmount")
