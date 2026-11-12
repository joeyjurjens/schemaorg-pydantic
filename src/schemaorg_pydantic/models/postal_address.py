from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .contact_point import ContactPoint

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .country import Country

if TYPE_CHECKING:
    AdministrativeArea_Text_Ref = Union[AdministrativeArea, Text, Ref]
else:
    AdministrativeArea_Text_Ref = Union[Is["AdministrativeArea"], Text, Ref]

if TYPE_CHECKING:
    Country_Text_Ref = Union[Country, Text, Ref]
else:
    Country_Text_Ref = Union[Is["Country"], Text, Ref]


class PostalAddress(ContactPoint):
    """The mailing address."""
    schema_type: ClassVar[str] = "PostalAddress"
    address_country: Country_Text_Ref | list[Country_Text_Ref] | None = Field(default=None, validation_alias="addressCountry", serialization_alias="addressCountry")
    address_locality: Text | list[Text] | None = Field(default=None, validation_alias="addressLocality", serialization_alias="addressLocality")
    address_region: AdministrativeArea_Text_Ref | list[AdministrativeArea_Text_Ref] | None = Field(default=None, validation_alias="addressRegion", serialization_alias="addressRegion")
    extended_address: Text | list[Text] | None = Field(default=None, validation_alias="extendedAddress", serialization_alias="extendedAddress")
    post_office_box_number: Text | list[Text] | None = Field(default=None, validation_alias="postOfficeBoxNumber", serialization_alias="postOfficeBoxNumber")
    postal_code: Text | list[Text] | None = Field(default=None, validation_alias="postalCode", serialization_alias="postalCode")
    street_address: Text | list[Text] | None = Field(default=None, validation_alias="streetAddress", serialization_alias="streetAddress")
