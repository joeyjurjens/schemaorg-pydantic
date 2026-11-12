from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .action import Action

if TYPE_CHECKING:
    from .price_specification import PriceSpecification

Number_Text = Union[Number, Text]
if TYPE_CHECKING:
    PriceSpecification_Ref = Union[PriceSpecification, Ref]
else:
    PriceSpecification_Ref = Union[Is["PriceSpecification"], Ref]


class TradeAction(Action):
    """The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment."""
    schema_type: ClassVar[str] = "TradeAction"
    price: Number_Text | list[Number_Text] | None = Field(default=None)
    price_currency: Text | list[Text] | None = Field(default=None, validation_alias="priceCurrency", serialization_alias="priceCurrency")
    price_specification: PriceSpecification_Ref | list[PriceSpecification_Ref] | None = Field(default=None, validation_alias="priceSpecification", serialization_alias="priceSpecification")
