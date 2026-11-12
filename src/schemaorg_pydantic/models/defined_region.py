from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .place import Place
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .country import Country
    from .postal_code_range_specification import PostalCodeRangeSpecification

if TYPE_CHECKING:
    AdministrativeArea_Text_Ref = Union[AdministrativeArea, Text, Ref]
else:
    AdministrativeArea_Text_Ref = Union[Is["AdministrativeArea"], Text, Ref]

if TYPE_CHECKING:
    Country_Text_Ref = Union[Country, Text, Ref]
else:
    Country_Text_Ref = Union[Is["Country"], Text, Ref]

if TYPE_CHECKING:
    PostalCodeRangeSpecification_Ref = Union[PostalCodeRangeSpecification, Ref]
else:
    PostalCodeRangeSpecification_Ref = Union[Is["PostalCodeRangeSpecification"], Ref]


class DefinedRegion(Place, StructuredValue):
    """A DefinedRegion is a geographic area defined by potentially arbitrary (rather than political, administrative or natural geographical) criteria. Properties are provided for defining a region by reference to sets of postal codes."""
    schema_type: ClassVar[str] = "DefinedRegion"
    address_country: Country_Text_Ref | list[Country_Text_Ref] | None = Field(default=None, validation_alias="addressCountry", serialization_alias="addressCountry")
    address_region: AdministrativeArea_Text_Ref | list[AdministrativeArea_Text_Ref] | None = Field(default=None, validation_alias="addressRegion", serialization_alias="addressRegion")
    postal_code: Text | list[Text] | None = Field(default=None, validation_alias="postalCode", serialization_alias="postalCode")
    postal_code_prefix: Text | list[Text] | None = Field(default=None, validation_alias="postalCodePrefix", serialization_alias="postalCodePrefix")
    postal_code_range: PostalCodeRangeSpecification_Ref | list[PostalCodeRangeSpecification_Ref] | None = Field(default=None, validation_alias="postalCodeRange", serialization_alias="postalCodeRange")
