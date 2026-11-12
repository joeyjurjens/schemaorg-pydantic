from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Is, Ref, Text, Time
from .intangible import Intangible
from .delivery_method import DeliveryMethod
from .item_availability import ItemAvailability
from .offer_item_condition import OfferItemCondition

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .aggregate_offer import AggregateOffer
    from .business_entity_type import BusinessEntityType
    from .business_function import BusinessFunction
    from .creative_work import CreativeWork
    from .event import Event
    from .geo_shape import GeoShape
    from .loan_or_credit import LoanOrCredit
    from .menu_item import MenuItem
    from .organization import Organization
    from .payment_method import PaymentMethod
    from .person import Person
    from .place import Place
    from .price_specification import PriceSpecification
    from .product import Product
    from .quantitative_value import QuantitativeValue
    from .service import Service
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
    BusinessEntityType_Ref = Union[BusinessEntityType, Ref]
else:
    BusinessEntityType_Ref = Union[Is["BusinessEntityType"], Ref]

if TYPE_CHECKING:
    BusinessFunction_Ref = Union[BusinessFunction, Ref]
else:
    BusinessFunction_Ref = Union[Is["BusinessFunction"], Ref]

Date_DateTime = Union[Date, DateTime]
Date_DateTime_Time = Union[Date, DateTime, Time]
if TYPE_CHECKING:
    GeoShape_Place_Text_Ref = Union[GeoShape, Place, Text, Ref]
else:
    GeoShape_Place_Text_Ref = Union[Is["GeoShape"], Is["Place"], Text, Ref]

if TYPE_CHECKING:
    LoanOrCredit_PaymentMethod_Text_Ref = Union[LoanOrCredit, PaymentMethod, Text, Ref]
else:
    LoanOrCredit_PaymentMethod_Text_Ref = Union[Is["LoanOrCredit"], Is["PaymentMethod"], Text, Ref]

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
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]

if TYPE_CHECKING:
    TypeAndQuantityNode_Ref = Union[TypeAndQuantityNode, Ref]
else:
    TypeAndQuantityNode_Ref = Union[Is["TypeAndQuantityNode"], Ref]

if TYPE_CHECKING:
    WarrantyPromise_Ref = Union[WarrantyPromise, Ref]
else:
    WarrantyPromise_Ref = Union[Is["WarrantyPromise"], Ref]


class Demand(Intangible):
    """A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply."""
    schema_type: ClassVar[str] = "Demand"
    accepted_payment_method: LoanOrCredit_PaymentMethod_Text_Ref | list[LoanOrCredit_PaymentMethod_Text_Ref] | None = Field(default=None, validation_alias="acceptedPaymentMethod", serialization_alias="acceptedPaymentMethod")
    advance_booking_requirement: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="advanceBookingRequirement", serialization_alias="advanceBookingRequirement")
    area_served: R3fcc4ec8 | list[R3fcc4ec8] | None = Field(default=None, validation_alias="areaServed", serialization_alias="areaServed")
    asin: Text | list[Text] | None = Field(default=None)
    availability: ItemAvailability | list[ItemAvailability] | None = Field(default=None)
    availability_ends: Date_DateTime_Time | list[Date_DateTime_Time] | None = Field(default=None, validation_alias="availabilityEnds", serialization_alias="availabilityEnds")
    availability_starts: Date_DateTime_Time | list[Date_DateTime_Time] | None = Field(default=None, validation_alias="availabilityStarts", serialization_alias="availabilityStarts")
    available_at_or_from: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="availableAtOrFrom", serialization_alias="availableAtOrFrom")
    available_delivery_method: DeliveryMethod | list[DeliveryMethod] | None = Field(default=None, validation_alias="availableDeliveryMethod", serialization_alias="availableDeliveryMethod")
    business_function: BusinessFunction_Ref | list[BusinessFunction_Ref] | None = Field(default=None, validation_alias="businessFunction", serialization_alias="businessFunction")
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
    includes_object: TypeAndQuantityNode_Ref | list[TypeAndQuantityNode_Ref] | None = Field(default=None, validation_alias="includesObject", serialization_alias="includesObject")
    ineligible_region: GeoShape_Place_Text_Ref | list[GeoShape_Place_Text_Ref] | None = Field(default=None, validation_alias="ineligibleRegion", serialization_alias="ineligibleRegion")
    inventory_level: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="inventoryLevel", serialization_alias="inventoryLevel")
    item_condition: OfferItemCondition | list[OfferItemCondition] | None = Field(default=None, validation_alias="itemCondition", serialization_alias="itemCondition")
    item_offered: Rf09a153a | list[Rf09a153a] | None = Field(default=None, validation_alias="itemOffered", serialization_alias="itemOffered")
    mpn: Text | list[Text] | None = Field(default=None)
    price_specification: PriceSpecification_Ref | list[PriceSpecification_Ref] | None = Field(default=None, validation_alias="priceSpecification", serialization_alias="priceSpecification")
    seller: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    serial_number: Text | list[Text] | None = Field(default=None, validation_alias="serialNumber", serialization_alias="serialNumber")
    sku: Text | list[Text] | None = Field(default=None)
    valid_from: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validFrom", serialization_alias="validFrom")
    valid_through: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validThrough", serialization_alias="validThrough")
    warranty: WarrantyPromise_Ref | list[WarrantyPromise_Ref] | None = Field(default=None)
