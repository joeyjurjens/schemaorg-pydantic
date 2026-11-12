from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text, Url
from .intangible import Intangible

if TYPE_CHECKING:
    from .contact_point import ContactPoint
    from .language import Language
    from .place import Place
    from .postal_address import PostalAddress
    from .service import Service

if TYPE_CHECKING:
    ContactPoint_Ref = Union[ContactPoint, Ref]
else:
    ContactPoint_Ref = Union[Is["ContactPoint"], Ref]

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]

if TYPE_CHECKING:
    Place_Ref = Union[Place, Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]

if TYPE_CHECKING:
    PostalAddress_Ref = Union[PostalAddress, Ref]
else:
    PostalAddress_Ref = Union[Is["PostalAddress"], Ref]

if TYPE_CHECKING:
    Service_Ref = Union[Service, Ref]
else:
    Service_Ref = Union[Is["Service"], Ref]


class ServiceChannel(Intangible):
    """A means for accessing a service, e.g. a government office location, web site, or phone number."""
    schema_type: ClassVar[str] = "ServiceChannel"
    available_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="availableLanguage", serialization_alias="availableLanguage")
    processing_time: Text | list[Text] | None = Field(default=None, validation_alias="processingTime", serialization_alias="processingTime")
    provides_service: Service_Ref | list[Service_Ref] | None = Field(default=None, validation_alias="providesService", serialization_alias="providesService")
    service_location: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="serviceLocation", serialization_alias="serviceLocation")
    service_phone: ContactPoint_Ref | list[ContactPoint_Ref] | None = Field(default=None, validation_alias="servicePhone", serialization_alias="servicePhone")
    service_postal_address: PostalAddress_Ref | list[PostalAddress_Ref] | None = Field(default=None, validation_alias="servicePostalAddress", serialization_alias="servicePostalAddress")
    service_sms_number: ContactPoint_Ref | list[ContactPoint_Ref] | None = Field(default=None, validation_alias="serviceSmsNumber", serialization_alias="serviceSmsNumber")
    service_url: Url | list[Url] | None = Field(default=None, validation_alias="serviceUrl", serialization_alias="serviceUrl")
