from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .business_function import BusinessFunction
    from .product import Product
    from .service import Service

if TYPE_CHECKING:
    BusinessFunction_Ref = Union[BusinessFunction, Ref]
else:
    BusinessFunction_Ref = Union[Is["BusinessFunction"], Ref]

if TYPE_CHECKING:
    Product_Service_Ref = Union[Product, Service, Ref]
else:
    Product_Service_Ref = Union[Is["Product"], Is["Service"], Ref]


class TypeAndQuantityNode(StructuredValue):
    """A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer."""
    schema_type: ClassVar[str] = "TypeAndQuantityNode"
    amount_of_this_good: Number | list[Number] | None = Field(default=None, validation_alias="amountOfThisGood", serialization_alias="amountOfThisGood")
    business_function: BusinessFunction_Ref | list[BusinessFunction_Ref] | None = Field(default=None, validation_alias="businessFunction", serialization_alias="businessFunction")
    type_of_good: Product_Service_Ref | list[Product_Service_Ref] | None = Field(default=None, validation_alias="typeOfGood", serialization_alias="typeOfGood")
    unit_code: Text | list[Text] | None = Field(default=None, validation_alias="unitCode", serialization_alias="unitCode")
    unit_text: Text | list[Text] | None = Field(default=None, validation_alias="unitText", serialization_alias="unitText")
