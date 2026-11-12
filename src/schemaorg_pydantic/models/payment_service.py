from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .financial_product import FinancialProduct
from .payment_method import PaymentMethod


class PaymentService(FinancialProduct, PaymentMethod):
    """A Service to transfer funds from a person or organization to a beneficiary person or organization."""
    schema_type: ClassVar[str] = "PaymentService"
