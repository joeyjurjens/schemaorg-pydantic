from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .financial_service import FinancialService


class AutomatedTeller(FinancialService):
    """ATM/cash machine."""
    schema_type: ClassVar[str] = "AutomatedTeller"
