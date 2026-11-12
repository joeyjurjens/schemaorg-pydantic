from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .collection import Collection
from .product import Product

if TYPE_CHECKING:
    from .type_and_quantity_node import TypeAndQuantityNode

if TYPE_CHECKING:
    TypeAndQuantityNode_Ref = Union[TypeAndQuantityNode, Ref]
else:
    TypeAndQuantityNode_Ref = Union[Is["TypeAndQuantityNode"], Ref]


class ProductCollection(Collection, Product):
    """A set of products (either [[ProductGroup]]s or specific variants) that are listed together e.g. in an [[Offer]]."""
    schema_type: ClassVar[str] = "ProductCollection"
    includes_object: TypeAndQuantityNode_Ref | list[TypeAndQuantityNode_Ref] | None = Field(default=None, validation_alias="includesObject", serialization_alias="includesObject")
