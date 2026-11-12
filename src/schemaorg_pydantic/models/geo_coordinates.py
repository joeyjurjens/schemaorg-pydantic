from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .country import Country
    from .postal_address import PostalAddress

if TYPE_CHECKING:
    Country_Text_Ref = Union[Country, Text, Ref]
else:
    Country_Text_Ref = Union[Is["Country"], Text, Ref]

Number_Text = Union[Number, Text]
if TYPE_CHECKING:
    PostalAddress_Text_Ref = Union[PostalAddress, Text, Ref]
else:
    PostalAddress_Text_Ref = Union[Is["PostalAddress"], Text, Ref]


class GeoCoordinates(StructuredValue):
    """The geographic coordinates of a place or event."""
    schema_type: ClassVar[str] = "GeoCoordinates"
    address: PostalAddress_Text_Ref | list[PostalAddress_Text_Ref] | None = Field(default=None)
    address_country: Country_Text_Ref | list[Country_Text_Ref] | None = Field(default=None, validation_alias="addressCountry", serialization_alias="addressCountry")
    elevation: Number_Text | list[Number_Text] | None = Field(default=None)
    latitude: Number_Text | list[Number_Text] | None = Field(default=None)
    longitude: Number_Text | list[Number_Text] | None = Field(default=None)
    postal_code: Text | list[Text] | None = Field(default=None, validation_alias="postalCode", serialization_alias="postalCode")
