from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .how_to_item import HowToItem

if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

if TYPE_CHECKING:
    MonetaryAmount_Text_Ref = Union[MonetaryAmount, Text, Ref]
else:
    MonetaryAmount_Text_Ref = Union[Is["MonetaryAmount"], Text, Ref]


class HowToSupply(HowToItem):
    """A supply consumed when performing the instructions for how to achieve a result."""
    schema_type: ClassVar[str] = "HowToSupply"
    estimated_cost: MonetaryAmount_Text_Ref | list[MonetaryAmount_Text_Ref] | None = Field(default=None, validation_alias="estimatedCost", serialization_alias="estimatedCost")
