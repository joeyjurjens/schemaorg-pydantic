from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text, Url
from .intangible import Intangible
from .government_benefits_type import GovernmentBenefitsType
from .physical_activity_category import PhysicalActivityCategory

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .aggregate_rating import AggregateRating
    from .audience import Audience
    from .brand import Brand
    from .category_code import CategoryCode
    from .certification import Certification
    from .demand import Demand
    from .geo_shape import GeoShape
    from .image_object import ImageObject
    from .offer import Offer
    from .offer_catalog import OfferCatalog
    from .opening_hours_specification import OpeningHoursSpecification
    from .organization import Organization
    from .person import Person
    from .place import Place
    from .product import Product
    from .review import Review
    from .service_channel import ServiceChannel
    from .thing import Thing

if TYPE_CHECKING:
    R3fcc4ec8 = Union[AdministrativeArea, GeoShape, Place, Text, Ref]
else:
    R3fcc4ec8 = Union[Is["AdministrativeArea"], Is["GeoShape"], Is["Place"], Text, Ref]

if TYPE_CHECKING:
    AggregateRating_Ref = Union[AggregateRating, Ref]
else:
    AggregateRating_Ref = Union[Is["AggregateRating"], Ref]

if TYPE_CHECKING:
    Audience_Ref = Union[Audience, Ref]
else:
    Audience_Ref = Union[Is["Audience"], Ref]

if TYPE_CHECKING:
    Brand_Organization_Ref = Union[Brand, Organization, Ref]
else:
    Brand_Organization_Ref = Union[Is["Brand"], Is["Organization"], Ref]

if TYPE_CHECKING:
    R88d1e012 = Union[CategoryCode, PhysicalActivityCategory, Thing, Text, Ref]
else:
    R88d1e012 = Union[Is["CategoryCode"], PhysicalActivityCategory, Is["Thing"], Text, Ref]

if TYPE_CHECKING:
    Certification_Ref = Union[Certification, Ref]
else:
    Certification_Ref = Union[Is["Certification"], Ref]

if TYPE_CHECKING:
    Demand_Offer_Ref = Union[Demand, Offer, Ref]
else:
    Demand_Offer_Ref = Union[Is["Demand"], Is["Offer"], Ref]

GovernmentBenefitsType_Text = Union[GovernmentBenefitsType, Text]
if TYPE_CHECKING:
    ImageObject_Url_Ref = Union[ImageObject, Url, Ref]
else:
    ImageObject_Url_Ref = Union[Is["ImageObject"], Url, Ref]

if TYPE_CHECKING:
    OfferCatalog_Ref = Union[OfferCatalog, Ref]
else:
    OfferCatalog_Ref = Union[Is["OfferCatalog"], Ref]

if TYPE_CHECKING:
    OpeningHoursSpecification_Ref = Union[OpeningHoursSpecification, Ref]
else:
    OpeningHoursSpecification_Ref = Union[Is["OpeningHoursSpecification"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Product_Service_Ref = Union[Product, "Service", Ref]
else:
    Product_Service_Ref = Union[Is["Product"], Is["Service"], Ref]

if TYPE_CHECKING:
    Review_Ref = Union[Review, Ref]
else:
    Review_Ref = Union[Is["Review"], Ref]

if TYPE_CHECKING:
    ServiceChannel_Ref = Union[ServiceChannel, Ref]
else:
    ServiceChannel_Ref = Union[Is["ServiceChannel"], Ref]

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]


class Service(Intangible):
    """A service provided by an organization, e.g. delivery service, print services, etc."""
    schema_type: ClassVar[str] = "Service"
    aggregate_rating: AggregateRating_Ref | list[AggregateRating_Ref] | None = Field(default=None, validation_alias="aggregateRating", serialization_alias="aggregateRating")
    area_served: R3fcc4ec8 | list[R3fcc4ec8] | None = Field(default=None, validation_alias="areaServed", serialization_alias="areaServed")
    audience: Audience_Ref | list[Audience_Ref] | None = Field(default=None)
    available_channel: ServiceChannel_Ref | list[ServiceChannel_Ref] | None = Field(default=None, validation_alias="availableChannel", serialization_alias="availableChannel")
    award: Text | list[Text] | None = Field(default=None)
    brand: Brand_Organization_Ref | list[Brand_Organization_Ref] | None = Field(default=None)
    broker: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    category: R88d1e012 | list[R88d1e012] | None = Field(default=None)
    has_certification: Certification_Ref | list[Certification_Ref] | None = Field(default=None, validation_alias="hasCertification", serialization_alias="hasCertification")
    has_offer_catalog: OfferCatalog_Ref | list[OfferCatalog_Ref] | None = Field(default=None, validation_alias="hasOfferCatalog", serialization_alias="hasOfferCatalog")
    hours_available: OpeningHoursSpecification_Ref | list[OpeningHoursSpecification_Ref] | None = Field(default=None, validation_alias="hoursAvailable", serialization_alias="hoursAvailable")
    is_related_to: Product_Service_Ref | list[Product_Service_Ref] | None = Field(default=None, validation_alias="isRelatedTo", serialization_alias="isRelatedTo")
    is_similar_to: Product_Service_Ref | list[Product_Service_Ref] | None = Field(default=None, validation_alias="isSimilarTo", serialization_alias="isSimilarTo")
    logo: ImageObject_Url_Ref | list[ImageObject_Url_Ref] | None = Field(default=None)
    offers: Demand_Offer_Ref | list[Demand_Offer_Ref] | None = Field(default=None)
    provider: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    provider_mobility: Text | list[Text] | None = Field(default=None, validation_alias="providerMobility", serialization_alias="providerMobility")
    review: Review_Ref | list[Review_Ref] | None = Field(default=None)
    service_output: Thing_Ref | list[Thing_Ref] | None = Field(default=None, validation_alias="serviceOutput", serialization_alias="serviceOutput")
    service_type: GovernmentBenefitsType_Text | list[GovernmentBenefitsType_Text] | None = Field(default=None, validation_alias="serviceType", serialization_alias="serviceType")
    slogan: Text | list[Text] | None = Field(default=None)
    terms_of_service: Text | list[Text] | None = Field(default=None, validation_alias="termsOfService", serialization_alias="termsOfService")
