from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Number, Ref, Text
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .defined_region import DefinedRegion
    from .delivery_charge_specification import DeliveryChargeSpecification
    from .monetary_amount import MonetaryAmount
    from .price_specification import PriceSpecification

if TYPE_CHECKING:
    DefinedRegion_Ref = Union[DefinedRegion, Ref]
else:
    DefinedRegion_Ref = Union[Is["DefinedRegion"], Ref]

if TYPE_CHECKING:
    DeliveryChargeSpecification_MonetaryAmount_Ref = Union[DeliveryChargeSpecification, MonetaryAmount, Ref]
else:
    DeliveryChargeSpecification_MonetaryAmount_Ref = Union[Is["DeliveryChargeSpecification"], Is["MonetaryAmount"], Ref]

if TYPE_CHECKING:
    MonetaryAmount_PriceSpecification_Number_Ref = Union[MonetaryAmount, PriceSpecification, Number, Ref]
else:
    MonetaryAmount_PriceSpecification_Number_Ref = Union[Is["MonetaryAmount"], Is["PriceSpecification"], Number, Ref]

if TYPE_CHECKING:
    MonetaryAmount_ShippingRateSettings_Ref = Union[MonetaryAmount, "ShippingRateSettings", Ref]
else:
    MonetaryAmount_ShippingRateSettings_Ref = Union[Is["MonetaryAmount"], Is["ShippingRateSettings"], Ref]


class ShippingRateSettings(StructuredValue):
    """A ShippingRateSettings represents re-usable pieces of shipping information. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished and matched (i.e. identified/referenced) by their different values for [[shippingLabel]]."""
    schema_type: ClassVar[str] = "ShippingRateSettings"
    does_not_ship: Boolean | list[Boolean] | None = Field(default=None, validation_alias="doesNotShip", serialization_alias="doesNotShip")
    free_shipping_threshold: DeliveryChargeSpecification_MonetaryAmount_Ref | list[DeliveryChargeSpecification_MonetaryAmount_Ref] | None = Field(default=None, validation_alias="freeShippingThreshold", serialization_alias="freeShippingThreshold")
    is_unlabelled_fallback: Boolean | list[Boolean] | None = Field(default=None, validation_alias="isUnlabelledFallback", serialization_alias="isUnlabelledFallback")
    minimum_order_value: MonetaryAmount_PriceSpecification_Number_Ref | list[MonetaryAmount_PriceSpecification_Number_Ref] | None = Field(default=None, validation_alias="minimumOrderValue", serialization_alias="minimumOrderValue")
    order_percentage: Number | list[Number] | None = Field(default=None, validation_alias="orderPercentage", serialization_alias="orderPercentage")
    shipping_destination: DefinedRegion_Ref | list[DefinedRegion_Ref] | None = Field(default=None, validation_alias="shippingDestination", serialization_alias="shippingDestination")
    shipping_label: Text | list[Text] | None = Field(default=None, validation_alias="shippingLabel", serialization_alias="shippingLabel")
    shipping_rate: MonetaryAmount_ShippingRateSettings_Ref | list[MonetaryAmount_ShippingRateSettings_Ref] | None = Field(default=None, validation_alias="shippingRate", serialization_alias="shippingRate")
    weight_percentage: Number | list[Number] | None = Field(default=None, validation_alias="weightPercentage", serialization_alias="weightPercentage")
