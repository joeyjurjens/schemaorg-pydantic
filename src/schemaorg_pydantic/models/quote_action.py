from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .trade_action import TradeAction


class QuoteAction(TradeAction):
    """An agent quotes/estimates/appraises an object/product/service with a price at a location/store."""
    schema_type: ClassVar[str] = "QuoteAction"
