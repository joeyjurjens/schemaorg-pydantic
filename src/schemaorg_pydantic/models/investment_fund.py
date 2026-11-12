from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .investment_or_deposit import InvestmentOrDeposit


class InvestmentFund(InvestmentOrDeposit):
    """A company or fund that gathers capital from a number of investors to create a pool of money that is then re-invested into stocks, bonds and other assets."""
    schema_type: ClassVar[str] = "InvestmentFund"
