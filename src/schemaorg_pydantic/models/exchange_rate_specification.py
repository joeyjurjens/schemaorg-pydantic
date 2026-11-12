from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount
    from .unit_price_specification import UnitPriceSpecification

if TYPE_CHECKING:
    MonetaryAmount_Number_Ref = Union[MonetaryAmount, Number, Ref]
else:
    MonetaryAmount_Number_Ref = Union[Is["MonetaryAmount"], Number, Ref]

if TYPE_CHECKING:
    UnitPriceSpecification_Ref = Union[UnitPriceSpecification, Ref]
else:
    UnitPriceSpecification_Ref = Union[Is["UnitPriceSpecification"], Ref]


class ExchangeRateSpecification(StructuredValue):
    """A structured value representing exchange rate."""
    schema_type: ClassVar[str] = "ExchangeRateSpecification"
    currency: Text | list[Text] | None = Field(default=None)
    current_exchange_rate: UnitPriceSpecification_Ref | list[UnitPriceSpecification_Ref] | None = Field(default=None, validation_alias="currentExchangeRate", serialization_alias="currentExchangeRate")
    exchange_rate_spread: MonetaryAmount_Number_Ref | list[MonetaryAmount_Number_Ref] | None = Field(default=None, validation_alias="exchangeRateSpread", serialization_alias="exchangeRateSpread")
