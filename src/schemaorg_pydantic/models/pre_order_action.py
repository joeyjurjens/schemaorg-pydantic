from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .trade_action import TradeAction


class PreOrderAction(TradeAction):
    """An agent orders a (not yet released) object/product/service to be delivered/sent."""
    schema_type: ClassVar[str] = "PreOrderAction"
