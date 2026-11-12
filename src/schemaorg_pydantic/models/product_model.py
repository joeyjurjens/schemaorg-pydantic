from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .product import Product

if TYPE_CHECKING:
    ProductModel_Ref = Union["ProductModel", Ref]
else:
    ProductModel_Ref = Union[Is["ProductModel"], Ref]


class ProductModel(Product):
    """A datasheet or vendor specification of a product (in the sense of a prototypical description)."""
    schema_type: ClassVar[str] = "ProductModel"
    predecessor_of: ProductModel_Ref | list[ProductModel_Ref] | None = Field(default=None, validation_alias="predecessorOf", serialization_alias="predecessorOf")
    successor_of: ProductModel_Ref | list[ProductModel_Ref] | None = Field(default=None, validation_alias="successorOf", serialization_alias="successorOf")
