from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Date, Is, Number, Ref, Text, Url
from .thing import Thing
from .adult_oriented_enumeration import AdultOrientedEnumeration
from .offer_item_condition import OfferItemCondition
from .physical_activity_category import PhysicalActivityCategory

if TYPE_CHECKING:
    from .aggregate_rating import AggregateRating
    from .audience import Audience
    from .brand import Brand
    from .category_code import CategoryCode
    from .certification import Certification
    from .chemical_substance import ChemicalSubstance
    from .country import Country
    from .defined_term import DefinedTerm
    from .demand import Demand
    from .digital_product_passport import DigitalProductPassport
    from .energy_consumption_details import EnergyConsumptionDetails
    from .grant import Grant
    from .image_object import ImageObject
    from .item_list import ItemList
    from .list_item import ListItem
    from .merchant_return_policy import MerchantReturnPolicy
    from .offer import Offer
    from .organization import Organization
    from .person import Person
    from .place import Place
    from .product_group import ProductGroup
    from .product_model import ProductModel
    from .property_value import PropertyValue
    from .quantitative_value import QuantitativeValue
    from .review import Review
    from .service import Service
    from .size_specification import SizeSpecification
    from .text_object import TextObject
    from .web_content import WebContent

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
    ChemicalSubstance_DefinedTerm_Text_Ref = Union[ChemicalSubstance, DefinedTerm, Text, Ref]
else:
    ChemicalSubstance_DefinedTerm_Text_Ref = Union[Is["ChemicalSubstance"], Is["DefinedTerm"], Text, Ref]

if TYPE_CHECKING:
    Country_Ref = Union[Country, Ref]
else:
    Country_Ref = Union[Is["Country"], Ref]

if TYPE_CHECKING:
    R5bddb616 = Union[DefinedTerm, QuantitativeValue, SizeSpecification, Text, Ref]
else:
    R5bddb616 = Union[Is["DefinedTerm"], Is["QuantitativeValue"], Is["SizeSpecification"], Text, Ref]

if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]

if TYPE_CHECKING:
    Demand_Offer_Ref = Union[Demand, Offer, Ref]
else:
    Demand_Offer_Ref = Union[Is["Demand"], Is["Offer"], Ref]

if TYPE_CHECKING:
    DigitalProductPassport_Url_Ref = Union[DigitalProductPassport, Url, Ref]
else:
    DigitalProductPassport_Url_Ref = Union[Is["DigitalProductPassport"], Url, Ref]

if TYPE_CHECKING:
    EnergyConsumptionDetails_Ref = Union[EnergyConsumptionDetails, Ref]
else:
    EnergyConsumptionDetails_Ref = Union[Is["EnergyConsumptionDetails"], Ref]

if TYPE_CHECKING:
    Grant_Ref = Union[Grant, Ref]
else:
    Grant_Ref = Union[Is["Grant"], Ref]

if TYPE_CHECKING:
    ImageObject_Url_Ref = Union[ImageObject, Url, Ref]
else:
    ImageObject_Url_Ref = Union[Is["ImageObject"], Url, Ref]

if TYPE_CHECKING:
    R318be025 = Union[ItemList, ListItem, WebContent, Text, Ref]
else:
    R318be025 = Union[Is["ItemList"], Is["ListItem"], Is["WebContent"], Text, Ref]

if TYPE_CHECKING:
    MerchantReturnPolicy_Ref = Union[MerchantReturnPolicy, Ref]
else:
    MerchantReturnPolicy_Ref = Union[Is["MerchantReturnPolicy"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]

if TYPE_CHECKING:
    Place_Ref = Union[Place, Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]

if TYPE_CHECKING:
    Product_Ref = Union["Product", Ref]
else:
    Product_Ref = Union[Is["Product"], Ref]

if TYPE_CHECKING:
    Product_Service_Ref = Union["Product", Service, Ref]
else:
    Product_Service_Ref = Union[Is["Product"], Is["Service"], Ref]

if TYPE_CHECKING:
    Product_Text_Ref = Union["Product", Text, Ref]
else:
    Product_Text_Ref = Union[Is["Product"], Text, Ref]

if TYPE_CHECKING:
    ProductGroup_ProductModel_Ref = Union[ProductGroup, ProductModel, Ref]
else:
    ProductGroup_ProductModel_Ref = Union[Is["ProductGroup"], Is["ProductModel"], Ref]

if TYPE_CHECKING:
    ProductModel_Text_Ref = Union[ProductModel, Text, Ref]
else:
    ProductModel_Text_Ref = Union[Is["ProductModel"], Text, Ref]

if TYPE_CHECKING:
    PropertyValue_Ref = Union[PropertyValue, Ref]
else:
    PropertyValue_Ref = Union[Is["PropertyValue"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]

if TYPE_CHECKING:
    Review_Ref = Union[Review, Ref]
else:
    Review_Ref = Union[Is["Review"], Ref]

if TYPE_CHECKING:
    TextObject_WebContent_Text_Ref = Union[TextObject, WebContent, Text, Ref]
else:
    TextObject_WebContent_Text_Ref = Union[Is["TextObject"], Is["WebContent"], Text, Ref]


class Product(Thing):
    """Any offered product or service. For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online."""
    schema_type: ClassVar[str] = "Product"
    additional_property: PropertyValue_Ref | list[PropertyValue_Ref] | None = Field(default=None, validation_alias="additionalProperty", serialization_alias="additionalProperty")
    aggregate_rating: AggregateRating_Ref | list[AggregateRating_Ref] | None = Field(default=None, validation_alias="aggregateRating", serialization_alias="aggregateRating")
    asin: Text | list[Text] | None = Field(default=None)
    audience: Audience_Ref | list[Audience_Ref] | None = Field(default=None)
    authorized_representative: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="authorizedRepresentative", serialization_alias="authorizedRepresentative")
    award: Text | list[Text] | None = Field(default=None)
    brand: Brand_Organization_Ref | list[Brand_Organization_Ref] | None = Field(default=None)
    category: R88d1e012 | list[R88d1e012] | None = Field(default=None)
    color: Text | list[Text] | None = Field(default=None)
    color_swatch: ImageObject_Url_Ref | list[ImageObject_Url_Ref] | None = Field(default=None, validation_alias="colorSwatch", serialization_alias="colorSwatch")
    consumer_notice: TextObject_WebContent_Text_Ref | list[TextObject_WebContent_Text_Ref] | None = Field(default=None, validation_alias="consumerNotice", serialization_alias="consumerNotice")
    country_of_assembly: Text | list[Text] | None = Field(default=None, validation_alias="countryOfAssembly", serialization_alias="countryOfAssembly")
    country_of_last_processing: Text | list[Text] | None = Field(default=None, validation_alias="countryOfLastProcessing", serialization_alias="countryOfLastProcessing")
    country_of_origin: Country_Ref | list[Country_Ref] | None = Field(default=None, validation_alias="countryOfOrigin", serialization_alias="countryOfOrigin")
    depth: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    display_location: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="displayLocation", serialization_alias="displayLocation")
    funding: Grant_Ref | list[Grant_Ref] | None = Field(default=None)
    gtin: Text | list[Text] | None = Field(default=None)
    gtin_12: Text | list[Text] | None = Field(default=None, validation_alias="gtin12", serialization_alias="gtin12")
    gtin_13: Text | list[Text] | None = Field(default=None, validation_alias="gtin13", serialization_alias="gtin13")
    gtin_14: Text | list[Text] | None = Field(default=None, validation_alias="gtin14", serialization_alias="gtin14")
    gtin_8: Text | list[Text] | None = Field(default=None, validation_alias="gtin8", serialization_alias="gtin8")
    has_adult_consideration: AdultOrientedEnumeration | list[AdultOrientedEnumeration] | None = Field(default=None, validation_alias="hasAdultConsideration", serialization_alias="hasAdultConsideration")
    has_certification: Certification_Ref | list[Certification_Ref] | None = Field(default=None, validation_alias="hasCertification", serialization_alias="hasCertification")
    has_digital_product_passport: DigitalProductPassport_Url_Ref | list[DigitalProductPassport_Url_Ref] | None = Field(default=None, validation_alias="hasDigitalProductPassport", serialization_alias="hasDigitalProductPassport")
    has_energy_consumption_details: EnergyConsumptionDetails_Ref | list[EnergyConsumptionDetails_Ref] | None = Field(default=None, validation_alias="hasEnergyConsumptionDetails", serialization_alias="hasEnergyConsumptionDetails")
    has_gs1_digital_link: Url | list[Url] | None = Field(default=None, validation_alias="hasGS1DigitalLink", serialization_alias="hasGS1DigitalLink")
    has_measurement: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="hasMeasurement", serialization_alias="hasMeasurement")
    has_merchant_return_policy: MerchantReturnPolicy_Ref | list[MerchantReturnPolicy_Ref] | None = Field(default=None, validation_alias="hasMerchantReturnPolicy", serialization_alias="hasMerchantReturnPolicy")
    height: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    importer: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    in_product_group_with_id: Text | list[Text] | None = Field(default=None, validation_alias="inProductGroupWithID", serialization_alias="inProductGroupWithID")
    is_accessory_or_spare_part_for: Product_Ref | list[Product_Ref] | None = Field(default=None, validation_alias="isAccessoryOrSparePartFor", serialization_alias="isAccessoryOrSparePartFor")
    is_consumable_for: Product_Ref | list[Product_Ref] | None = Field(default=None, validation_alias="isConsumableFor", serialization_alias="isConsumableFor")
    is_family_friendly: Boolean | list[Boolean] | None = Field(default=None, validation_alias="isFamilyFriendly", serialization_alias="isFamilyFriendly")
    is_often_bought_with: Product_Ref | list[Product_Ref] | None = Field(default=None, validation_alias="isOftenBoughtWith", serialization_alias="isOftenBoughtWith")
    is_related_to: Product_Service_Ref | list[Product_Service_Ref] | None = Field(default=None, validation_alias="isRelatedTo", serialization_alias="isRelatedTo")
    is_similar_to: Product_Service_Ref | list[Product_Service_Ref] | None = Field(default=None, validation_alias="isSimilarTo", serialization_alias="isSimilarTo")
    is_variant_of: ProductGroup_ProductModel_Ref | list[ProductGroup_ProductModel_Ref] | None = Field(default=None, validation_alias="isVariantOf", serialization_alias="isVariantOf")
    item_condition: OfferItemCondition | list[OfferItemCondition] | None = Field(default=None, validation_alias="itemCondition", serialization_alias="itemCondition")
    keywords: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    logo: ImageObject_Url_Ref | list[ImageObject_Url_Ref] | None = Field(default=None)
    manufacturer: Organization_Ref | list[Organization_Ref] | None = Field(default=None)
    material: Product_Text_Ref | list[Product_Text_Ref] | None = Field(default=None)
    mobile_url: Text | list[Text] | None = Field(default=None, validation_alias="mobileUrl", serialization_alias="mobileUrl")
    model: ProductModel_Text_Ref | list[ProductModel_Text_Ref] | None = Field(default=None)
    mpn: Text | list[Text] | None = Field(default=None)
    negative_notes: R318be025 | list[R318be025] | None = Field(default=None, validation_alias="negativeNotes", serialization_alias="negativeNotes")
    nsn: Text | list[Text] | None = Field(default=None)
    offers: Demand_Offer_Ref | list[Demand_Offer_Ref] | None = Field(default=None)
    pattern: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    positive_notes: R318be025 | list[R318be025] | None = Field(default=None, validation_alias="positiveNotes", serialization_alias="positiveNotes")
    product_id: Text | list[Text] | None = Field(default=None, validation_alias="productID", serialization_alias="productID")
    production_date: Date | list[Date] | None = Field(default=None, validation_alias="productionDate", serialization_alias="productionDate")
    purchase_date: Date | list[Date] | None = Field(default=None, validation_alias="purchaseDate", serialization_alias="purchaseDate")
    recycled_content_percentage: Number | list[Number] | None = Field(default=None, validation_alias="recycledContentPercentage", serialization_alias="recycledContentPercentage")
    release_date: Date | list[Date] | None = Field(default=None, validation_alias="releaseDate", serialization_alias="releaseDate")
    review: Review_Ref | list[Review_Ref] | None = Field(default=None)
    size: R5bddb616 | list[R5bddb616] | None = Field(default=None)
    sku: Text | list[Text] | None = Field(default=None)
    slogan: Text | list[Text] | None = Field(default=None)
    specification: PropertyValue_Ref | list[PropertyValue_Ref] | None = Field(default=None)
    substance_of_concern: ChemicalSubstance_DefinedTerm_Text_Ref | list[ChemicalSubstance_DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="substanceOfConcern", serialization_alias="substanceOfConcern")
    weight: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    width: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
