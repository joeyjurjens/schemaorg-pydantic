from __future__ import annotations

from typing import ClassVar, Union

from pydantic import Field

from ..base import Date, DateTime, Time
from .structured_value import StructuredValue
from .day_of_week import DayOfWeek

Date_DateTime = Union[Date, DateTime]

class OpeningHoursSpecification(StructuredValue):
    """A structured value providing information about the opening hours of a place or a certain service inside a place."""
    schema_type: ClassVar[str] = "OpeningHoursSpecification"
    closes: Time | list[Time] | None = Field(default=None)
    day_of_week: DayOfWeek | list[DayOfWeek] | None = Field(default=None, validation_alias="dayOfWeek", serialization_alias="dayOfWeek")
    opens: Time | list[Time] | None = Field(default=None)
    valid_from: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validFrom", serialization_alias="validFrom")
    valid_through: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validThrough", serialization_alias="validThrough")
