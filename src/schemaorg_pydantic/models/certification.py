from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Is, Ref, Text, Url
from .creative_work import CreativeWork
from .certification_status_enumeration import CertificationStatusEnumeration

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .defined_term import DefinedTerm
    from .image_object import ImageObject
    from .organization import Organization
    from .quantitative_value import QuantitativeValue
    from .rating import Rating

if TYPE_CHECKING:
    AdministrativeArea_Ref = Union[AdministrativeArea, Ref]
else:
    AdministrativeArea_Ref = Union[Is["AdministrativeArea"], Ref]

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]

if TYPE_CHECKING:
    ImageObject_Url_Ref = Union[ImageObject, Url, Ref]
else:
    ImageObject_Url_Ref = Union[Is["ImageObject"], Url, Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]

if TYPE_CHECKING:
    Rating_Ref = Union[Rating, Ref]
else:
    Rating_Ref = Union[Is["Rating"], Ref]


class Certification(CreativeWork):
    """A Certification is an official and authoritative statement about a subject, for example a product, service, person, or organization. A certification is typically issued by an indendent certification body, for example a professional organization or government. It formally attests certain characteristics about the subject, for example Organizations can be ISO certified, Food products can be certified Organic or Vegan, a Person can be a certified professional, a Place can be certified for food processing. There are certifications for many domains: regulatory, organizational, recycling, food, efficiency, educational, ecological, etc. A certification is a form of credential, as are accreditations and licenses. Mapped from the [gs1:CertificationDetails](https://www.gs1.org/voc/CertificationDetails) class in the GS1 Web Vocabulary."""
    schema_type: ClassVar[str] = "Certification"
    audit_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="auditDate", serialization_alias="auditDate")
    certification_identification: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="certificationIdentification", serialization_alias="certificationIdentification")
    certification_rating: Rating_Ref | list[Rating_Ref] | None = Field(default=None, validation_alias="certificationRating", serialization_alias="certificationRating")
    certification_status: CertificationStatusEnumeration | list[CertificationStatusEnumeration] | None = Field(default=None, validation_alias="certificationStatus", serialization_alias="certificationStatus")
    has_measurement: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="hasMeasurement", serialization_alias="hasMeasurement")
    issued_by: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="issuedBy", serialization_alias="issuedBy")
    logo: ImageObject_Url_Ref | list[ImageObject_Url_Ref] | None = Field(default=None)
    valid_from: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validFrom", serialization_alias="validFrom")
    valid_in: AdministrativeArea_Ref | list[AdministrativeArea_Ref] | None = Field(default=None, validation_alias="validIn", serialization_alias="validIn")
