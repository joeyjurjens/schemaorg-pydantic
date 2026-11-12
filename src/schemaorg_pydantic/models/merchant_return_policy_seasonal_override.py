from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Integer, Is, Number, Ref
from .intangible import Intangible
from .merchant_return_enumeration import MerchantReturnEnumeration
from .refund_type_enumeration import RefundTypeEnumeration
from .return_fees_enumeration import ReturnFeesEnumeration
from .return_method_enumeration import ReturnMethodEnumeration

if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

Date_DateTime = Union[Date, DateTime]
Date_DateTime_Integer = Union[Date, DateTime, Integer]
if TYPE_CHECKING:
    MonetaryAmount_Number_Ref = Union[MonetaryAmount, Number, Ref]
else:
    MonetaryAmount_Number_Ref = Union[Is["MonetaryAmount"], Number, Ref]

if TYPE_CHECKING:
    MonetaryAmount_Ref = Union[MonetaryAmount, Ref]
else:
    MonetaryAmount_Ref = Union[Is["MonetaryAmount"], Ref]


class MerchantReturnPolicySeasonalOverride(Intangible):
    """A seasonal override of a return policy, for example used for holidays."""
    schema_type: ClassVar[str] = "MerchantReturnPolicySeasonalOverride"
    end_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="endDate", serialization_alias="endDate")
    merchant_return_days: Date_DateTime_Integer | list[Date_DateTime_Integer] | None = Field(default=None, validation_alias="merchantReturnDays", serialization_alias="merchantReturnDays")
    refund_type: RefundTypeEnumeration | list[RefundTypeEnumeration] | None = Field(default=None, validation_alias="refundType", serialization_alias="refundType")
    restocking_fee: MonetaryAmount_Number_Ref | list[MonetaryAmount_Number_Ref] | None = Field(default=None, validation_alias="restockingFee", serialization_alias="restockingFee")
    return_fees: ReturnFeesEnumeration | list[ReturnFeesEnumeration] | None = Field(default=None, validation_alias="returnFees", serialization_alias="returnFees")
    return_method: ReturnMethodEnumeration | list[ReturnMethodEnumeration] | None = Field(default=None, validation_alias="returnMethod", serialization_alias="returnMethod")
    return_policy_category: MerchantReturnEnumeration | list[MerchantReturnEnumeration] | None = Field(default=None, validation_alias="returnPolicyCategory", serialization_alias="returnPolicyCategory")
    return_shipping_fees_amount: MonetaryAmount_Ref | list[MonetaryAmount_Ref] | None = Field(default=None, validation_alias="returnShippingFeesAmount", serialization_alias="returnShippingFeesAmount")
    start_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="startDate", serialization_alias="startDate")
