from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Integer, Is, Ref, Text, Time
from .intangible import Intangible
from .day_of_week import DayOfWeek

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

Date_DateTime = Union[Date, DateTime]
DateTime_Time = Union[DateTime, Time]
DayOfWeek_Text = Union[DayOfWeek, Text]
if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class Schedule(Intangible):
    """A schedule defines a repeating time period used to describe a regularly occurring [[Event]]. At a minimum a schedule will specify [[repeatFrequency]] which describes the interval between occurrences of the event. Additional information can be provided to specify the schedule more precisely.\n      This includes identifying the day(s) of the week or month when the recurring event will take place, in addition to its start and end time. Schedules may also\n      have start and end dates to indicate when they are active, e.g. to define a limited calendar of events."""
    schema_type: ClassVar[str] = "Schedule"
    by_day: DayOfWeek_Text | list[DayOfWeek_Text] | None = Field(default=None, validation_alias="byDay", serialization_alias="byDay")
    by_month: Integer | list[Integer] | None = Field(default=None, validation_alias="byMonth", serialization_alias="byMonth")
    by_month_day: Integer | list[Integer] | None = Field(default=None, validation_alias="byMonthDay", serialization_alias="byMonthDay")
    by_month_week: Integer | list[Integer] | None = Field(default=None, validation_alias="byMonthWeek", serialization_alias="byMonthWeek")
    duration: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    end_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="endDate", serialization_alias="endDate")
    end_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="endTime", serialization_alias="endTime")
    except_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="exceptDate", serialization_alias="exceptDate")
    repeat_count: Integer | list[Integer] | None = Field(default=None, validation_alias="repeatCount", serialization_alias="repeatCount")
    repeat_frequency: Text | list[Text] | None = Field(default=None, validation_alias="repeatFrequency", serialization_alias="repeatFrequency")
    schedule_timezone: Text | list[Text] | None = Field(default=None, validation_alias="scheduleTimezone", serialization_alias="scheduleTimezone")
    start_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="startDate", serialization_alias="startDate")
    start_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="startTime", serialization_alias="startTime")
