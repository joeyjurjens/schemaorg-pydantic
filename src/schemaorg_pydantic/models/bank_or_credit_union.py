from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .financial_service import FinancialService


class BankOrCreditUnion(FinancialService):
    """Bank or credit union."""
    schema_type: ClassVar[str] = "BankOrCreditUnion"
