from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Date, DateTime, Integer, Is, Number, Ref, Text, Url
from .intangible import Intangible
from .merchant_return_enumeration import MerchantReturnEnumeration
from .offer_item_condition import OfferItemCondition
from .refund_type_enumeration import RefundTypeEnumeration
from .return_fees_enumeration import ReturnFeesEnumeration
from .return_label_source_enumeration import ReturnLabelSourceEnumeration
from .return_method_enumeration import ReturnMethodEnumeration

if TYPE_CHECKING:
    from .country import Country
    from .member_program_tier import MemberProgramTier
    from .merchant_return_policy_seasonal_override import MerchantReturnPolicySeasonalOverride
    from .monetary_amount import MonetaryAmount
    from .property_value import PropertyValue

if TYPE_CHECKING:
    Country_Text_Ref = Union[Country, Text, Ref]
else:
    Country_Text_Ref = Union[Is["Country"], Text, Ref]

Date_DateTime_Integer = Union[Date, DateTime, Integer]
if TYPE_CHECKING:
    MemberProgramTier_Ref = Union[MemberProgramTier, Ref]
else:
    MemberProgramTier_Ref = Union[Is["MemberProgramTier"], Ref]

if TYPE_CHECKING:
    MerchantReturnPolicySeasonalOverride_Ref = Union[MerchantReturnPolicySeasonalOverride, Ref]
else:
    MerchantReturnPolicySeasonalOverride_Ref = Union[Is["MerchantReturnPolicySeasonalOverride"], Ref]

if TYPE_CHECKING:
    MonetaryAmount_Number_Ref = Union[MonetaryAmount, Number, Ref]
else:
    MonetaryAmount_Number_Ref = Union[Is["MonetaryAmount"], Number, Ref]

if TYPE_CHECKING:
    MonetaryAmount_Ref = Union[MonetaryAmount, Ref]
else:
    MonetaryAmount_Ref = Union[Is["MonetaryAmount"], Ref]

if TYPE_CHECKING:
    PropertyValue_Ref = Union[PropertyValue, Ref]
else:
    PropertyValue_Ref = Union[Is["PropertyValue"], Ref]


class MerchantReturnPolicy(Intangible):
    """A MerchantReturnPolicy provides information about product return policies associated with an [[Organization]], [[Product]], or [[Offer]]."""
    schema_type: ClassVar[str] = "MerchantReturnPolicy"
    additional_property: PropertyValue_Ref | list[PropertyValue_Ref] | None = Field(default=None, validation_alias="additionalProperty", serialization_alias="additionalProperty")
    applicable_country: Country_Text_Ref | list[Country_Text_Ref] | None = Field(default=None, validation_alias="applicableCountry", serialization_alias="applicableCountry")
    customer_remorse_return_fees: ReturnFeesEnumeration | list[ReturnFeesEnumeration] | None = Field(default=None, validation_alias="customerRemorseReturnFees", serialization_alias="customerRemorseReturnFees")
    customer_remorse_return_label_source: ReturnLabelSourceEnumeration | list[ReturnLabelSourceEnumeration] | None = Field(default=None, validation_alias="customerRemorseReturnLabelSource", serialization_alias="customerRemorseReturnLabelSource")
    customer_remorse_return_shipping_fees_amount: MonetaryAmount_Ref | list[MonetaryAmount_Ref] | None = Field(default=None, validation_alias="customerRemorseReturnShippingFeesAmount", serialization_alias="customerRemorseReturnShippingFeesAmount")
    in_store_returns_offered: Boolean | list[Boolean] | None = Field(default=None, validation_alias="inStoreReturnsOffered", serialization_alias="inStoreReturnsOffered")
    item_condition: OfferItemCondition | list[OfferItemCondition] | None = Field(default=None, validation_alias="itemCondition", serialization_alias="itemCondition")
    item_defect_return_fees: ReturnFeesEnumeration | list[ReturnFeesEnumeration] | None = Field(default=None, validation_alias="itemDefectReturnFees", serialization_alias="itemDefectReturnFees")
    item_defect_return_label_source: ReturnLabelSourceEnumeration | list[ReturnLabelSourceEnumeration] | None = Field(default=None, validation_alias="itemDefectReturnLabelSource", serialization_alias="itemDefectReturnLabelSource")
    item_defect_return_shipping_fees_amount: MonetaryAmount_Ref | list[MonetaryAmount_Ref] | None = Field(default=None, validation_alias="itemDefectReturnShippingFeesAmount", serialization_alias="itemDefectReturnShippingFeesAmount")
    merchant_return_days: Date_DateTime_Integer | list[Date_DateTime_Integer] | None = Field(default=None, validation_alias="merchantReturnDays", serialization_alias="merchantReturnDays")
    merchant_return_link: Url | list[Url] | None = Field(default=None, validation_alias="merchantReturnLink", serialization_alias="merchantReturnLink")
    refund_type: RefundTypeEnumeration | list[RefundTypeEnumeration] | None = Field(default=None, validation_alias="refundType", serialization_alias="refundType")
    restocking_fee: MonetaryAmount_Number_Ref | list[MonetaryAmount_Number_Ref] | None = Field(default=None, validation_alias="restockingFee", serialization_alias="restockingFee")
    return_fees: ReturnFeesEnumeration | list[ReturnFeesEnumeration] | None = Field(default=None, validation_alias="returnFees", serialization_alias="returnFees")
    return_label_source: ReturnLabelSourceEnumeration | list[ReturnLabelSourceEnumeration] | None = Field(default=None, validation_alias="returnLabelSource", serialization_alias="returnLabelSource")
    return_method: ReturnMethodEnumeration | list[ReturnMethodEnumeration] | None = Field(default=None, validation_alias="returnMethod", serialization_alias="returnMethod")
    return_policy_category: MerchantReturnEnumeration | list[MerchantReturnEnumeration] | None = Field(default=None, validation_alias="returnPolicyCategory", serialization_alias="returnPolicyCategory")
    return_policy_country: Country_Text_Ref | list[Country_Text_Ref] | None = Field(default=None, validation_alias="returnPolicyCountry", serialization_alias="returnPolicyCountry")
    return_policy_seasonal_override: MerchantReturnPolicySeasonalOverride_Ref | list[MerchantReturnPolicySeasonalOverride_Ref] | None = Field(default=None, validation_alias="returnPolicySeasonalOverride", serialization_alias="returnPolicySeasonalOverride")
    return_shipping_fees_amount: MonetaryAmount_Ref | list[MonetaryAmount_Ref] | None = Field(default=None, validation_alias="returnShippingFeesAmount", serialization_alias="returnShippingFeesAmount")
    valid_for_member_tier: MemberProgramTier_Ref | list[MemberProgramTier_Ref] | None = Field(default=None, validation_alias="validForMemberTier", serialization_alias="validForMemberTier")
