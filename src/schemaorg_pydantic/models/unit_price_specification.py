from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .price_specification import PriceSpecification
from .price_component_type_enumeration import PriceComponentTypeEnumeration
from .price_type_enumeration import PriceTypeEnumeration

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

PriceTypeEnumeration_Text = Union[PriceTypeEnumeration, Text]
if TYPE_CHECKING:
    QuantitativeValue_Number_Text_Ref = Union[QuantitativeValue, Number, Text, Ref]
else:
    QuantitativeValue_Number_Text_Ref = Union[Is["QuantitativeValue"], Number, Text, Ref]

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]


class UnitPriceSpecification(PriceSpecification):
    """The price asked for a given offer by the respective organization or person."""
    schema_type: ClassVar[str] = "UnitPriceSpecification"
    billing_duration: QuantitativeValue_Number_Text_Ref | list[QuantitativeValue_Number_Text_Ref] | None = Field(default=None, validation_alias="billingDuration", serialization_alias="billingDuration")
    billing_increment: Number | list[Number] | None = Field(default=None, validation_alias="billingIncrement", serialization_alias="billingIncrement")
    billing_start: Number | list[Number] | None = Field(default=None, validation_alias="billingStart", serialization_alias="billingStart")
    price_component_type: PriceComponentTypeEnumeration | list[PriceComponentTypeEnumeration] | None = Field(default=None, validation_alias="priceComponentType", serialization_alias="priceComponentType")
    price_type: PriceTypeEnumeration_Text | list[PriceTypeEnumeration_Text] | None = Field(default=None, validation_alias="priceType", serialization_alias="priceType")
    reference_quantity: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="referenceQuantity", serialization_alias="referenceQuantity")
    unit_code: Text | list[Text] | None = Field(default=None, validation_alias="unitCode", serialization_alias="unitCode")
    unit_text: Text | list[Text] | None = Field(default=None, validation_alias="unitText", serialization_alias="unitText")
