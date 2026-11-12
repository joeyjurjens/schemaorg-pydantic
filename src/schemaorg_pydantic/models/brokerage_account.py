from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .investment_or_deposit import InvestmentOrDeposit


class BrokerageAccount(InvestmentOrDeposit):
    """An account that allows an investor to deposit funds and place investment orders with a licensed broker or brokerage firm."""
    schema_type: ClassVar[str] = "BrokerageAccount"
