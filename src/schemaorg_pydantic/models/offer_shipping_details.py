from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Ref, Text, Url
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .defined_region import DefinedRegion
    from .member_program_tier import MemberProgramTier
    from .monetary_amount import MonetaryAmount
    from .organization import Organization
    from .person import Person
    from .quantitative_value import QuantitativeValue
    from .shipping_delivery_time import ShippingDeliveryTime
    from .shipping_rate_settings import ShippingRateSettings
    from .shipping_service import ShippingService

if TYPE_CHECKING:
    DefinedRegion_Ref = Union[DefinedRegion, Ref]
else:
    DefinedRegion_Ref = Union[Is["DefinedRegion"], Ref]

if TYPE_CHECKING:
    MemberProgramTier_Ref = Union[MemberProgramTier, Ref]
else:
    MemberProgramTier_Ref = Union[Is["MemberProgramTier"], Ref]

if TYPE_CHECKING:
    MonetaryAmount_ShippingRateSettings_Ref = Union[MonetaryAmount, ShippingRateSettings, Ref]
else:
    MonetaryAmount_ShippingRateSettings_Ref = Union[Is["MonetaryAmount"], Is["ShippingRateSettings"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]

if TYPE_CHECKING:
    ShippingDeliveryTime_Ref = Union[ShippingDeliveryTime, Ref]
else:
    ShippingDeliveryTime_Ref = Union[Is["ShippingDeliveryTime"], Ref]

if TYPE_CHECKING:
    ShippingService_Ref = Union[ShippingService, Ref]
else:
    ShippingService_Ref = Union[Is["ShippingService"], Ref]


class OfferShippingDetails(StructuredValue):
    """OfferShippingDetails represents information about shipping destinations."""
    schema_type: ClassVar[str] = "OfferShippingDetails"
    delivery_time: ShippingDeliveryTime_Ref | list[ShippingDeliveryTime_Ref] | None = Field(default=None, validation_alias="deliveryTime", serialization_alias="deliveryTime")
    depth: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    does_not_ship: Boolean | list[Boolean] | None = Field(default=None, validation_alias="doesNotShip", serialization_alias="doesNotShip")
    has_shipping_service: ShippingService_Ref | list[ShippingService_Ref] | None = Field(default=None, validation_alias="hasShippingService", serialization_alias="hasShippingService")
    height: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    provider: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    shipping_destination: DefinedRegion_Ref | list[DefinedRegion_Ref] | None = Field(default=None, validation_alias="shippingDestination", serialization_alias="shippingDestination")
    shipping_label: Text | list[Text] | None = Field(default=None, validation_alias="shippingLabel", serialization_alias="shippingLabel")
    shipping_origin: DefinedRegion_Ref | list[DefinedRegion_Ref] | None = Field(default=None, validation_alias="shippingOrigin", serialization_alias="shippingOrigin")
    shipping_rate: MonetaryAmount_ShippingRateSettings_Ref | list[MonetaryAmount_ShippingRateSettings_Ref] | None = Field(default=None, validation_alias="shippingRate", serialization_alias="shippingRate")
    shipping_settings_link: Url | list[Url] | None = Field(default=None, validation_alias="shippingSettingsLink", serialization_alias="shippingSettingsLink")
    transit_time_label: Text | list[Text] | None = Field(default=None, validation_alias="transitTimeLabel", serialization_alias="transitTimeLabel")
    valid_for_member_tier: MemberProgramTier_Ref | list[MemberProgramTier_Ref] | None = Field(default=None, validation_alias="validForMemberTier", serialization_alias="validForMemberTier")
    weight: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    width: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
