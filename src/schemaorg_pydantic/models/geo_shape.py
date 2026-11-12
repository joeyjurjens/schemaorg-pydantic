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


class GeoShape(StructuredValue):
    """The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points."""
    schema_type: ClassVar[str] = "GeoShape"
    address: PostalAddress_Text_Ref | list[PostalAddress_Text_Ref] | None = Field(default=None)
    address_country: Country_Text_Ref | list[Country_Text_Ref] | None = Field(default=None, validation_alias="addressCountry", serialization_alias="addressCountry")
    box: Text | list[Text] | None = Field(default=None)
    circle: Text | list[Text] | None = Field(default=None)
    elevation: Number_Text | list[Number_Text] | None = Field(default=None)
    line: Text | list[Text] | None = Field(default=None)
    polygon: Text | list[Text] | None = Field(default=None)
    postal_code: Text | list[Text] | None = Field(default=None, validation_alias="postalCode", serialization_alias="postalCode")
