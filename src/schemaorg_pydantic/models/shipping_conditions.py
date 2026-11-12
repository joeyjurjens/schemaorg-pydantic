from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Ref, Text
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .defined_region import DefinedRegion
    from .monetary_amount import MonetaryAmount
    from .opening_hours_specification import OpeningHoursSpecification
    from .quantitative_value import QuantitativeValue
    from .service_period import ServicePeriod
    from .shipping_rate_settings import ShippingRateSettings

if TYPE_CHECKING:
    DefinedRegion_Ref = Union[DefinedRegion, Ref]
else:
    DefinedRegion_Ref = Union[Is["DefinedRegion"], Ref]

if TYPE_CHECKING:
    MonetaryAmount_Ref = Union[MonetaryAmount, Ref]
else:
    MonetaryAmount_Ref = Union[Is["MonetaryAmount"], Ref]

if TYPE_CHECKING:
    MonetaryAmount_ShippingRateSettings_Ref = Union[MonetaryAmount, ShippingRateSettings, Ref]
else:
    MonetaryAmount_ShippingRateSettings_Ref = Union[Is["MonetaryAmount"], Is["ShippingRateSettings"], Ref]

if TYPE_CHECKING:
    OpeningHoursSpecification_Ref = Union[OpeningHoursSpecification, Ref]
else:
    OpeningHoursSpecification_Ref = Union[Is["OpeningHoursSpecification"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_ServicePeriod_Ref = Union[QuantitativeValue, ServicePeriod, Ref]
else:
    QuantitativeValue_ServicePeriod_Ref = Union[Is["QuantitativeValue"], Is["ServicePeriod"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class ShippingConditions(StructuredValue):
    """ShippingConditions represent a set of constraints and information about the conditions of shipping a product. Such conditions may apply to only a subset of the products being shipped, depending on aspects of the product like weight, size, price, destination, and others. All the specified conditions must be met for this ShippingConditions to apply."""
    schema_type: ClassVar[str] = "ShippingConditions"
    depth: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    does_not_ship: Boolean | list[Boolean] | None = Field(default=None, validation_alias="doesNotShip", serialization_alias="doesNotShip")
    height: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    num_items: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="numItems", serialization_alias="numItems")
    order_value: MonetaryAmount_Ref | list[MonetaryAmount_Ref] | None = Field(default=None, validation_alias="orderValue", serialization_alias="orderValue")
    seasonal_override: OpeningHoursSpecification_Ref | list[OpeningHoursSpecification_Ref] | None = Field(default=None, validation_alias="seasonalOverride", serialization_alias="seasonalOverride")
    shipping_destination: DefinedRegion_Ref | list[DefinedRegion_Ref] | None = Field(default=None, validation_alias="shippingDestination", serialization_alias="shippingDestination")
    shipping_origin: DefinedRegion_Ref | list[DefinedRegion_Ref] | None = Field(default=None, validation_alias="shippingOrigin", serialization_alias="shippingOrigin")
    shipping_rate: MonetaryAmount_ShippingRateSettings_Ref | list[MonetaryAmount_ShippingRateSettings_Ref] | None = Field(default=None, validation_alias="shippingRate", serialization_alias="shippingRate")
    transit_time: QuantitativeValue_ServicePeriod_Ref | list[QuantitativeValue_ServicePeriod_Ref] | None = Field(default=None, validation_alias="transitTime", serialization_alias="transitTime")
    weight: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    width: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
