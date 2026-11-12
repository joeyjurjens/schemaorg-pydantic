from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Number, Ref, Text
from .offer import Offer

if TYPE_CHECKING:
    from .demand import Demand

if TYPE_CHECKING:
    Demand_Offer_Ref = Union[Demand, Offer, Ref]
else:
    Demand_Offer_Ref = Union[Is["Demand"], Is["Offer"], Ref]

Number_Text = Union[Number, Text]

class AggregateOffer(Offer):
    """When a single product is associated with multiple offers (for example, the same pair of shoes is offered by different merchants), then AggregateOffer can be used."""
    schema_type: ClassVar[str] = "AggregateOffer"
    high_price: Number_Text | list[Number_Text] | None = Field(default=None, validation_alias="highPrice", serialization_alias="highPrice")
    low_price: Number_Text | list[Number_Text] | None = Field(default=None, validation_alias="lowPrice", serialization_alias="lowPrice")
    offer_count: Integer | list[Integer] | None = Field(default=None, validation_alias="offerCount", serialization_alias="offerCount")
    offers: Demand_Offer_Ref | list[Demand_Offer_Ref] | None = Field(default=None)
