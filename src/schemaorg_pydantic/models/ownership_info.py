from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import DateTime, Is, Ref
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person
    from .product import Product
    from .service import Service

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Product_Service_Ref = Union[Product, Service, Ref]
else:
    Product_Service_Ref = Union[Is["Product"], Is["Service"], Ref]


class OwnershipInfo(StructuredValue):
    """A structured value providing information about when a certain organization or person owned a certain product."""
    schema_type: ClassVar[str] = "OwnershipInfo"
    acquired_from: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="acquiredFrom", serialization_alias="acquiredFrom")
    owned_from: DateTime | list[DateTime] | None = Field(default=None, validation_alias="ownedFrom", serialization_alias="ownedFrom")
    owned_through: DateTime | list[DateTime] | None = Field(default=None, validation_alias="ownedThrough", serialization_alias="ownedThrough")
    type_of_good: Product_Service_Ref | list[Product_Service_Ref] | None = Field(default=None, validation_alias="typeOfGood", serialization_alias="typeOfGood")
