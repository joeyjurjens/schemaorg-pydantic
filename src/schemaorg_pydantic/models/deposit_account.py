from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .bank_account import BankAccount
from .investment_or_deposit import InvestmentOrDeposit


class DepositAccount(BankAccount, InvestmentOrDeposit):
    """A type of Bank Account with a main purpose of depositing funds to gain interest or other benefits."""
    schema_type: ClassVar[str] = "DepositAccount"
