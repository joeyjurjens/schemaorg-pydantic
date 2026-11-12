from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .organization import Organization


class Corporation(Organization):
    """Organization: A business corporation."""
    schema_type: ClassVar[str] = "Corporation"
    ticker_symbol: Text | list[Text] | None = Field(default=None, validation_alias="tickerSymbol", serialization_alias="tickerSymbol")
