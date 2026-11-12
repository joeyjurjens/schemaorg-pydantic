from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .loan_or_credit import LoanOrCredit
from .payment_card import PaymentCard


class CreditCard(LoanOrCredit, PaymentCard):
    """A card payment method of a particular brand or name.  Used to mark up a particular payment method and/or the financial product/service that supplies the card account."""
    schema_type: ClassVar[str] = "CreditCard"
