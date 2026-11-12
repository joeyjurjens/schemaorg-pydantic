from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .structured_value import StructuredValue
from .contact_point_option import ContactPointOption

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .geo_shape import GeoShape
    from .language import Language
    from .opening_hours_specification import OpeningHoursSpecification
    from .place import Place
    from .product import Product

if TYPE_CHECKING:
    R3fcc4ec8 = Union[AdministrativeArea, GeoShape, Place, Text, Ref]
else:
    R3fcc4ec8 = Union[Is["AdministrativeArea"], Is["GeoShape"], Is["Place"], Text, Ref]

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]

if TYPE_CHECKING:
    OpeningHoursSpecification_Ref = Union[OpeningHoursSpecification, Ref]
else:
    OpeningHoursSpecification_Ref = Union[Is["OpeningHoursSpecification"], Ref]

if TYPE_CHECKING:
    Product_Text_Ref = Union[Product, Text, Ref]
else:
    Product_Text_Ref = Union[Is["Product"], Text, Ref]


class ContactPoint(StructuredValue):
    """A contact point&#x2014;for example, a Customer Complaints department."""
    schema_type: ClassVar[str] = "ContactPoint"
    area_served: R3fcc4ec8 | list[R3fcc4ec8] | None = Field(default=None, validation_alias="areaServed", serialization_alias="areaServed")
    available_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="availableLanguage", serialization_alias="availableLanguage")
    contact_option: ContactPointOption | list[ContactPointOption] | None = Field(default=None, validation_alias="contactOption", serialization_alias="contactOption")
    contact_type: Text | list[Text] | None = Field(default=None, validation_alias="contactType", serialization_alias="contactType")
    email: Text | list[Text] | None = Field(default=None)
    fax_number: Text | list[Text] | None = Field(default=None, validation_alias="faxNumber", serialization_alias="faxNumber")
    hours_available: OpeningHoursSpecification_Ref | list[OpeningHoursSpecification_Ref] | None = Field(default=None, validation_alias="hoursAvailable", serialization_alias="hoursAvailable")
    product_supported: Product_Text_Ref | list[Product_Text_Ref] | None = Field(default=None, validation_alias="productSupported", serialization_alias="productSupported")
    telephone: Text | list[Text] | None = Field(default=None)
