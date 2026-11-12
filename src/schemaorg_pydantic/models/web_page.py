from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, Is, Ref, Text, Url
from .creative_work import CreativeWork
from .medical_specialty import MedicalSpecialty

if TYPE_CHECKING:
    from .breadcrumb_list import BreadcrumbList
    from .image_object import ImageObject
    from .organization import Organization
    from .person import Person
    from .speakable_specification import SpeakableSpecification
    from .web_page_element import WebPageElement

if TYPE_CHECKING:
    BreadcrumbList_Text_Ref = Union[BreadcrumbList, Text, Ref]
else:
    BreadcrumbList_Text_Ref = Union[Is["BreadcrumbList"], Text, Ref]

if TYPE_CHECKING:
    ImageObject_Ref = Union[ImageObject, Ref]
else:
    ImageObject_Ref = Union[Is["ImageObject"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    SpeakableSpecification_Url_Ref = Union[SpeakableSpecification, Url, Ref]
else:
    SpeakableSpecification_Url_Ref = Union[Is["SpeakableSpecification"], Url, Ref]

if TYPE_CHECKING:
    WebPageElement_Ref = Union[WebPageElement, Ref]
else:
    WebPageElement_Ref = Union[Is["WebPageElement"], Ref]


class WebPage(CreativeWork):
    """A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page."""
    schema_type: ClassVar[str] = "WebPage"
    breadcrumb: BreadcrumbList_Text_Ref | list[BreadcrumbList_Text_Ref] | None = Field(default=None)
    last_reviewed: Date | list[Date] | None = Field(default=None, validation_alias="lastReviewed", serialization_alias="lastReviewed")
    main_content_of_page: WebPageElement_Ref | list[WebPageElement_Ref] | None = Field(default=None, validation_alias="mainContentOfPage", serialization_alias="mainContentOfPage")
    primary_image_of_page: ImageObject_Ref | list[ImageObject_Ref] | None = Field(default=None, validation_alias="primaryImageOfPage", serialization_alias="primaryImageOfPage")
    related_link: Url | list[Url] | None = Field(default=None, validation_alias="relatedLink", serialization_alias="relatedLink")
    reviewed_by: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="reviewedBy", serialization_alias="reviewedBy")
    significant_link: Url | list[Url] | None = Field(default=None, validation_alias="significantLink", serialization_alias="significantLink")
    speakable: SpeakableSpecification_Url_Ref | list[SpeakableSpecification_Url_Ref] | None = Field(default=None)
    specialty: MedicalSpecialty | list[MedicalSpecialty] | None = Field(default=None)
