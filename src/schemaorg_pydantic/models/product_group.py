from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .product import Product

if TYPE_CHECKING:
    from .defined_term import DefinedTerm
    from .property_value import PropertyValue

if TYPE_CHECKING:
    DefinedTerm_PropertyValue_Text_Ref = Union[DefinedTerm, PropertyValue, Text, Ref]
else:
    DefinedTerm_PropertyValue_Text_Ref = Union[Is["DefinedTerm"], Is["PropertyValue"], Text, Ref]

if TYPE_CHECKING:
    Product_Ref = Union[Product, Ref]
else:
    Product_Ref = Union[Is["Product"], Ref]


class ProductGroup(Product):
    """A ProductGroup represents a group of [[Product]]s that vary only in certain well-described ways, such as by [[size]], [[color]], [[material]] etc."""
    schema_type: ClassVar[str] = "ProductGroup"
    has_variant: Product_Ref | list[Product_Ref] | None = Field(default=None, validation_alias="hasVariant", serialization_alias="hasVariant")
    product_group_id: Text | list[Text] | None = Field(default=None, validation_alias="productGroupID", serialization_alias="productGroupID")
    varies_by: DefinedTerm_PropertyValue_Text_Ref | list[DefinedTerm_PropertyValue_Text_Ref] | None = Field(default=None, validation_alias="variesBy", serialization_alias="variesBy")
