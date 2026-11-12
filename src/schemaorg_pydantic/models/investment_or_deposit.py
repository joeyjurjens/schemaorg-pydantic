from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref
from .financial_product import FinancialProduct

if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

if TYPE_CHECKING:
    MonetaryAmount_Number_Ref = Union[MonetaryAmount, Number, Ref]
else:
    MonetaryAmount_Number_Ref = Union[Is["MonetaryAmount"], Number, Ref]


class InvestmentOrDeposit(FinancialProduct):
    """A type of financial product that typically requires the client to transfer funds to a financial service in return for potential beneficial financial return."""
    schema_type: ClassVar[str] = "InvestmentOrDeposit"
    amount: MonetaryAmount_Number_Ref | list[MonetaryAmount_Number_Ref] | None = Field(default=None)
