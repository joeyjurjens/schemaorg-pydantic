from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .quantitative_value_distribution import QuantitativeValueDistribution


class MonetaryAmountDistribution(QuantitativeValueDistribution):
    """A statistical distribution of monetary amounts."""
    schema_type: ClassVar[str] = "MonetaryAmountDistribution"
    currency: Text | list[Text] | None = Field(default=None)
