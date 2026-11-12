from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Date, DateTime, Is, Number, Ref, Text, Time, Url
from .intangible import Intangible
from .adult_oriented_enumeration import AdultOrientedEnumeration
from .delivery_method import DeliveryMethod
from .item_availability import ItemAvailability
from .offer_item_condition import OfferItemCondition
from .physical_activity_category import PhysicalActivityCategory

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .aggregate_offer import AggregateOffer
    from .aggregate_rating import AggregateRating
    from .business_entity_type import BusinessEntityType
    from .business_function import BusinessFunction
    from .category_code import CategoryCode
    from .creative_work import CreativeWork
    from .digital_product_passport import DigitalProductPassport
    from .event import Event
    from .geo_shape import GeoShape
    from .loan_or_credit import LoanOrCredit
    from .member_program_tier import MemberProgramTier
    from .menu_item import MenuItem
    from .merchant_return_policy import MerchantReturnPolicy
    from .offer_shipping_details import OfferShippingDetails
    from .organization import Organization
    from .payment_method import PaymentMethod
    from .person import Person
    from .place import Place
    from .price_specification import PriceSpecification
    from .product import Product
    from .property_value import PropertyValue
    from .quantitative_value import QuantitativeValue
    from .review import Review
    from .service import Service
    from .thing import Thing
    from .trip import Trip
    from .type_and_quantity_node import TypeAndQuantityNode
    from .warranty_promise import WarrantyPromise

if TYPE_CHECKING:
    R3fcc4ec8 = Union[AdministrativeArea, GeoShape, Place, Text, Ref]
else:
    R3fcc4ec8 = Union[Is["AdministrativeArea"], Is["GeoShape"], Is["Place"], Text, Ref]

if TYPE_CHECKING:
    Rf09a153a = Union[AggregateOffer, CreativeWork, Event, MenuItem, Product, Service, Trip, Ref]
else:
    Rf09a153a = Union[Is["AggregateOffer"], Is["CreativeWork"], Is["Event"], Is["MenuItem"], Is["Product"], Is["Service"], Is["Trip"], Ref]

if TYPE_CHECKING:
    AggregateRating_Ref = Union[AggregateRating, Ref]
else:
    AggregateRating_Ref = Union[Is["AggregateRating"], Ref]

if TYPE_CHECKING:
    BusinessEntityType_Ref = Union[BusinessEntityType, Ref]
else:
    BusinessEntityType_Ref = Union[Is["BusinessEntityType"], Ref]

if TYPE_CHECKING:
    BusinessFunction_Ref = Union[BusinessFunction, Ref]
else:
    BusinessFunction_Ref = Union[Is["BusinessFunction"], Ref]

if TYPE_CHECKING:
    R88d1e012 = Union[CategoryCode, PhysicalActivityCategory, Thing, Text, Ref]
else:
    R88d1e012 = Union[Is["CategoryCode"], PhysicalActivityCategory, Is["Thing"], Text, Ref]

Date_DateTime = Union[Date, DateTime]
Date_DateTime_Time = Union[Date, DateTime, Time]
if TYPE_CHECKING:
    DigitalProductPassport_Url_Ref = Union[DigitalProductPassport, Url, Ref]
else:
    DigitalProductPassport_Url_Ref = Union[Is["DigitalProductPassport"], Url, Ref]

if TYPE_CHECKING:
    GeoShape_Place_Text_Ref = Union[GeoShape, Place, Text, Ref]
else:
    GeoShape_Place_Text_Ref = Union[Is["GeoShape"], Is["Place"], Text, Ref]

if TYPE_CHECKING:
    LoanOrCredit_PaymentMethod_Text_Ref = Union[LoanOrCredit, PaymentMethod, Text, Ref]
else:
    LoanOrCredit_PaymentMethod_Text_Ref = Union[Is["LoanOrCredit"], Is["PaymentMethod"], Text, Ref]

if TYPE_CHECKING:
    MemberProgramTier_Ref = Union[MemberProgramTier, Ref]
else:
    MemberProgramTier_Ref = Union[Is["MemberProgramTier"], Ref]

if TYPE_CHECKING:
    MerchantReturnPolicy_Ref = Union[MerchantReturnPolicy, Ref]
else:
    MerchantReturnPolicy_Ref = Union[Is["MerchantReturnPolicy"], Ref]

Number_Text = Union[Number, Text]
if TYPE_CHECKING:
    Offer_Ref = Union["Offer", Ref]
else:
    Offer_Ref = Union[Is["Offer"], Ref]

if TYPE_CHECKING:
    OfferShippingDetails_Ref = Union[OfferShippingDetails, Ref]
else:
    OfferShippingDetails_Ref = Union[Is["OfferShippingDetails"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Place_Ref = Union[Place, Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]

if TYPE_CHECKING:
    PriceSpecification_Ref = Union[PriceSpecification, Ref]
else:
    PriceSpecification_Ref = Union[Is["PriceSpecification"], Ref]

if TYPE_CHECKING:
    PropertyValue_Ref = Union[PropertyValue, Ref]
else:
    PropertyValue_Ref = Union[Is["PropertyValue"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Number_Ref = Union[QuantitativeValue, Number, Ref]
else:
    QuantitativeValue_Number_Ref = Union[Is["QuantitativeValue"], Number, Ref]

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
    TypeAndQuantityNode_Ref = Union[TypeAndQuantityNode, Ref]
else:
    TypeAndQuantityNode_Ref = Union[Is["TypeAndQuantityNode"], Ref]

if TYPE_CHECKING:
    WarrantyPromise_Ref = Union[WarrantyPromise, Ref]
else:
    WarrantyPromise_Ref = Union[Is["WarrantyPromise"], Ref]


class Offer(Intangible):
    """An offer to transfer some rights to an item or to provide a service \u2014 for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book."""
    schema_type: ClassVar[str] = "Offer"
    accepted_payment_method: LoanOrCredit_PaymentMethod_Text_Ref | list[LoanOrCredit_PaymentMethod_Text_Ref] | None = Field(default=None, validation_alias="acceptedPaymentMethod", serialization_alias="acceptedPaymentMethod")
    add_on: Offer_Ref | list[Offer_Ref] | None = Field(default=None, validation_alias="addOn", serialization_alias="addOn")
    additional_property: PropertyValue_Ref | list[PropertyValue_Ref] | None = Field(default=None, validation_alias="additionalProperty", serialization_alias="additionalProperty")
    advance_booking_requirement: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="advanceBookingRequirement", serialization_alias="advanceBookingRequirement")
    aggregate_rating: AggregateRating_Ref | list[AggregateRating_Ref] | None = Field(default=None, validation_alias="aggregateRating", serialization_alias="aggregateRating")
    area_served: R3fcc4ec8 | list[R3fcc4ec8] | None = Field(default=None, validation_alias="areaServed", serialization_alias="areaServed")
    asin: Text | list[Text] | None = Field(default=None)
    availability: ItemAvailability | list[ItemAvailability] | None = Field(default=None)
    availability_ends: Date_DateTime_Time | list[Date_DateTime_Time] | None = Field(default=None, validation_alias="availabilityEnds", serialization_alias="availabilityEnds")
    availability_starts: Date_DateTime_Time | list[Date_DateTime_Time] | None = Field(default=None, validation_alias="availabilityStarts", serialization_alias="availabilityStarts")
    available_at_or_from: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="availableAtOrFrom", serialization_alias="availableAtOrFrom")
    available_delivery_method: DeliveryMethod | list[DeliveryMethod] | None = Field(default=None, validation_alias="availableDeliveryMethod", serialization_alias="availableDeliveryMethod")
    business_function: BusinessFunction_Ref | list[BusinessFunction_Ref] | None = Field(default=None, validation_alias="businessFunction", serialization_alias="businessFunction")
    category: R88d1e012 | list[R88d1e012] | None = Field(default=None)
    checkout_page_url_template: Text | list[Text] | None = Field(default=None, validation_alias="checkoutPageURLTemplate", serialization_alias="checkoutPageURLTemplate")
    delivery_lead_time: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="deliveryLeadTime", serialization_alias="deliveryLeadTime")
    eligible_customer_type: BusinessEntityType_Ref | list[BusinessEntityType_Ref] | None = Field(default=None, validation_alias="eligibleCustomerType", serialization_alias="eligibleCustomerType")
    eligible_duration: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="eligibleDuration", serialization_alias="eligibleDuration")
    eligible_quantity: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="eligibleQuantity", serialization_alias="eligibleQuantity")
    eligible_region: GeoShape_Place_Text_Ref | list[GeoShape_Place_Text_Ref] | None = Field(default=None, validation_alias="eligibleRegion", serialization_alias="eligibleRegion")
    eligible_transaction_volume: PriceSpecification_Ref | list[PriceSpecification_Ref] | None = Field(default=None, validation_alias="eligibleTransactionVolume", serialization_alias="eligibleTransactionVolume")
    gtin: Text | list[Text] | None = Field(default=None)
    gtin_12: Text | list[Text] | None = Field(default=None, validation_alias="gtin12", serialization_alias="gtin12")
    gtin_13: Text | list[Text] | None = Field(default=None, validation_alias="gtin13", serialization_alias="gtin13")
    gtin_14: Text | list[Text] | None = Field(default=None, validation_alias="gtin14", serialization_alias="gtin14")
    gtin_8: Text | list[Text] | None = Field(default=None, validation_alias="gtin8", serialization_alias="gtin8")
    has_adult_consideration: AdultOrientedEnumeration | list[AdultOrientedEnumeration] | None = Field(default=None, validation_alias="hasAdultConsideration", serialization_alias="hasAdultConsideration")
    has_digital_product_passport: DigitalProductPassport_Url_Ref | list[DigitalProductPassport_Url_Ref] | None = Field(default=None, validation_alias="hasDigitalProductPassport", serialization_alias="hasDigitalProductPassport")
    has_gs1_digital_link: Url | list[Url] | None = Field(default=None, validation_alias="hasGS1DigitalLink", serialization_alias="hasGS1DigitalLink")
    has_measurement: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="hasMeasurement", serialization_alias="hasMeasurement")
    has_merchant_return_policy: MerchantReturnPolicy_Ref | list[MerchantReturnPolicy_Ref] | None = Field(default=None, validation_alias="hasMerchantReturnPolicy", serialization_alias="hasMerchantReturnPolicy")
    includes_object: TypeAndQuantityNode_Ref | list[TypeAndQuantityNode_Ref] | None = Field(default=None, validation_alias="includesObject", serialization_alias="includesObject")
    ineligible_region: GeoShape_Place_Text_Ref | list[GeoShape_Place_Text_Ref] | None = Field(default=None, validation_alias="ineligibleRegion", serialization_alias="ineligibleRegion")
    inventory_level: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="inventoryLevel", serialization_alias="inventoryLevel")
    is_family_friendly: Boolean | list[Boolean] | None = Field(default=None, validation_alias="isFamilyFriendly", serialization_alias="isFamilyFriendly")
    item_condition: OfferItemCondition | list[OfferItemCondition] | None = Field(default=None, validation_alias="itemCondition", serialization_alias="itemCondition")
    item_offered: Rf09a153a | list[Rf09a153a] | None = Field(default=None, validation_alias="itemOffered", serialization_alias="itemOffered")
    item_popularity: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="itemPopularity", serialization_alias="itemPopularity")
    lease_length: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None, validation_alias="leaseLength", serialization_alias="leaseLength")
    mobile_url: Text | list[Text] | None = Field(default=None, validation_alias="mobileUrl", serialization_alias="mobileUrl")
    mpn: Text | list[Text] | None = Field(default=None)
    offered_by: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="offeredBy", serialization_alias="offeredBy")
    price: Number_Text | list[Number_Text] | None = Field(default=None)
    price_currency: Text | list[Text] | None = Field(default=None, validation_alias="priceCurrency", serialization_alias="priceCurrency")
    price_specification: PriceSpecification_Ref | list[PriceSpecification_Ref] | None = Field(default=None, validation_alias="priceSpecification", serialization_alias="priceSpecification")
    price_valid_until: Date | list[Date] | None = Field(default=None, validation_alias="priceValidUntil", serialization_alias="priceValidUntil")
    review: Review_Ref | list[Review_Ref] | None = Field(default=None)
    seller: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    serial_number: Text | list[Text] | None = Field(default=None, validation_alias="serialNumber", serialization_alias="serialNumber")
    shipping_details: OfferShippingDetails_Ref | list[OfferShippingDetails_Ref] | None = Field(default=None, validation_alias="shippingDetails", serialization_alias="shippingDetails")
    sku: Text | list[Text] | None = Field(default=None)
    valid_for_member_tier: MemberProgramTier_Ref | list[MemberProgramTier_Ref] | None = Field(default=None, validation_alias="validForMemberTier", serialization_alias="validForMemberTier")
    valid_from: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validFrom", serialization_alias="validFrom")
    valid_through: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validThrough", serialization_alias="validThrough")
    warranty: WarrantyPromise_Ref | list[WarrantyPromise_Ref] | None = Field(default=None)
