from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .financial_service import FinancialService


class AccountingService(FinancialService):
    """Accountancy business."""
    schema_type: ClassVar[str] = "AccountingService"
