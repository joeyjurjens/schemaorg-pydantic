from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .financial_product import FinancialProduct

if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

if TYPE_CHECKING:
    MonetaryAmount_Ref = Union[MonetaryAmount, Ref]
else:
    MonetaryAmount_Ref = Union[Is["MonetaryAmount"], Ref]


class BankAccount(FinancialProduct):
    """A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be paid interest."""
    schema_type: ClassVar[str] = "BankAccount"
    account_minimum_inflow: MonetaryAmount_Ref | list[MonetaryAmount_Ref] | None = Field(default=None, validation_alias="accountMinimumInflow", serialization_alias="accountMinimumInflow")
    account_overdraft_limit: MonetaryAmount_Ref | list[MonetaryAmount_Ref] | None = Field(default=None, validation_alias="accountOverdraftLimit", serialization_alias="accountOverdraftLimit")
    bank_account_type: Text | list[Text] | None = Field(default=None, validation_alias="bankAccountType", serialization_alias="bankAccountType")
