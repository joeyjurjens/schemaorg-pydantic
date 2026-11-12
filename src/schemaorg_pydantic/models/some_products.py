from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .product import Product

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]


class SomeProducts(Product):
    """A placeholder for multiple similar products of the same kind."""
    schema_type: ClassVar[str] = "SomeProducts"
    inventory_level: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="inventoryLevel", serialization_alias="inventoryLevel")
