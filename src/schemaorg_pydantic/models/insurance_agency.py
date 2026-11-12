from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .financial_service import FinancialService


class InsuranceAgency(FinancialService):
    """An Insurance agency."""
    schema_type: ClassVar[str] = "InsuranceAgency"
