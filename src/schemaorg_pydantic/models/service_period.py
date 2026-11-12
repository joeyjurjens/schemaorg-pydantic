from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text, Time
from .structured_value import StructuredValue
from .day_of_week import DayOfWeek

if TYPE_CHECKING:
    from .opening_hours_specification import OpeningHoursSpecification
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    DayOfWeek_OpeningHoursSpecification_Ref = Union[DayOfWeek, OpeningHoursSpecification, Ref]
else:
    DayOfWeek_OpeningHoursSpecification_Ref = Union[DayOfWeek, Is["OpeningHoursSpecification"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class ServicePeriod(StructuredValue):
    """ServicePeriod represents a duration with some constraints about cutoff time and business days. This is used e.g. in shipping for handling times or transit time."""
    schema_type: ClassVar[str] = "ServicePeriod"
    business_days: DayOfWeek_OpeningHoursSpecification_Ref | list[DayOfWeek_OpeningHoursSpecification_Ref] | None = Field(default=None, validation_alias="businessDays", serialization_alias="businessDays")
    cutoff_time: Time | list[Time] | None = Field(default=None, validation_alias="cutoffTime", serialization_alias="cutoffTime")
    duration: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
