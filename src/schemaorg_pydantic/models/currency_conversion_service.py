from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .financial_product import FinancialProduct


class CurrencyConversionService(FinancialProduct):
    """A service to convert funds from one currency to another currency."""
    schema_type: ClassVar[str] = "CurrencyConversionService"
