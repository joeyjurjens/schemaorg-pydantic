from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Time
from .structured_value import StructuredValue
from .day_of_week import DayOfWeek

if TYPE_CHECKING:
    from .opening_hours_specification import OpeningHoursSpecification
    from .quantitative_value import QuantitativeValue
    from .service_period import ServicePeriod

if TYPE_CHECKING:
    DayOfWeek_OpeningHoursSpecification_Ref = Union[DayOfWeek, OpeningHoursSpecification, Ref]
else:
    DayOfWeek_OpeningHoursSpecification_Ref = Union[DayOfWeek, Is["OpeningHoursSpecification"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_ServicePeriod_Ref = Union[QuantitativeValue, ServicePeriod, Ref]
else:
    QuantitativeValue_ServicePeriod_Ref = Union[Is["QuantitativeValue"], Is["ServicePeriod"], Ref]


class ShippingDeliveryTime(StructuredValue):
    """ShippingDeliveryTime provides various pieces of information about delivery times for shipping."""
    schema_type: ClassVar[str] = "ShippingDeliveryTime"
    business_days: DayOfWeek_OpeningHoursSpecification_Ref | list[DayOfWeek_OpeningHoursSpecification_Ref] | None = Field(default=None, validation_alias="businessDays", serialization_alias="businessDays")
    cutoff_time: Time | list[Time] | None = Field(default=None, validation_alias="cutoffTime", serialization_alias="cutoffTime")
    handling_time: QuantitativeValue_ServicePeriod_Ref | list[QuantitativeValue_ServicePeriod_Ref] | None = Field(default=None, validation_alias="handlingTime", serialization_alias="handlingTime")
    transit_time: QuantitativeValue_ServicePeriod_Ref | list[QuantitativeValue_ServicePeriod_Ref] | None = Field(default=None, validation_alias="transitTime", serialization_alias="transitTime")
