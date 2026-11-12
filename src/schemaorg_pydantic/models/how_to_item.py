from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .list_item import ListItem

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    QuantitativeValue_Number_Text_Ref = Union[QuantitativeValue, Number, Text, Ref]
else:
    QuantitativeValue_Number_Text_Ref = Union[Is["QuantitativeValue"], Number, Text, Ref]


class HowToItem(ListItem):
    """An item used as either a tool or supply when performing the instructions for how to achieve a result."""
    schema_type: ClassVar[str] = "HowToItem"
    required_quantity: QuantitativeValue_Number_Text_Ref | list[QuantitativeValue_Number_Text_Ref] | None = Field(default=None, validation_alias="requiredQuantity", serialization_alias="requiredQuantity")
