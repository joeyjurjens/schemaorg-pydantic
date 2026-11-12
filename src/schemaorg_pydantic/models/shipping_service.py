from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .structured_value import StructuredValue
from .fulfillment_type_enumeration import FulfillmentTypeEnumeration

if TYPE_CHECKING:
    from .member_program_tier import MemberProgramTier
    from .quantitative_value import QuantitativeValue
    from .service_period import ServicePeriod
    from .shipping_conditions import ShippingConditions

if TYPE_CHECKING:
    MemberProgramTier_Ref = Union[MemberProgramTier, Ref]
else:
    MemberProgramTier_Ref = Union[Is["MemberProgramTier"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_ServicePeriod_Ref = Union[QuantitativeValue, ServicePeriod, Ref]
else:
    QuantitativeValue_ServicePeriod_Ref = Union[Is["QuantitativeValue"], Is["ServicePeriod"], Ref]

if TYPE_CHECKING:
    ShippingConditions_Ref = Union[ShippingConditions, Ref]
else:
    ShippingConditions_Ref = Union[Is["ShippingConditions"], Ref]


class ShippingService(StructuredValue):
    """ShippingService represents the criteria used to determine if and how an offer could be shipped to a customer."""
    schema_type: ClassVar[str] = "ShippingService"
    fulfillment_type: FulfillmentTypeEnumeration | list[FulfillmentTypeEnumeration] | None = Field(default=None, validation_alias="fulfillmentType", serialization_alias="fulfillmentType")
    handling_time: QuantitativeValue_ServicePeriod_Ref | list[QuantitativeValue_ServicePeriod_Ref] | None = Field(default=None, validation_alias="handlingTime", serialization_alias="handlingTime")
    shipping_conditions: ShippingConditions_Ref | list[ShippingConditions_Ref] | None = Field(default=None, validation_alias="shippingConditions", serialization_alias="shippingConditions")
    valid_for_member_tier: MemberProgramTier_Ref | list[MemberProgramTier_Ref] | None = Field(default=None, validation_alias="validForMemberTier", serialization_alias="validForMemberTier")
