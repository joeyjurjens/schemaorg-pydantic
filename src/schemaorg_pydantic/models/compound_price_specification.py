from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .price_specification import PriceSpecification
from .price_type_enumeration import PriceTypeEnumeration

if TYPE_CHECKING:
    PriceSpecification_Ref = Union[PriceSpecification, Ref]
else:
    PriceSpecification_Ref = Union[Is["PriceSpecification"], Ref]

PriceTypeEnumeration_Text = Union[PriceTypeEnumeration, Text]

class CompoundPriceSpecification(PriceSpecification):
    """A compound price specification is one that bundles multiple prices that all apply in combination for different dimensions of consumption. Use the name property of the attached unit price specification for indicating the dimension of a price component (e.g. \"electricity\" or \"final cleaning\")."""
    schema_type: ClassVar[str] = "CompoundPriceSpecification"
    price_component: PriceSpecification_Ref | list[PriceSpecification_Ref] | None = Field(default=None, validation_alias="priceComponent", serialization_alias="priceComponent")
    price_type: PriceTypeEnumeration_Text | list[PriceTypeEnumeration_Text] | None = Field(default=None, validation_alias="priceType", serialization_alias="priceType")
