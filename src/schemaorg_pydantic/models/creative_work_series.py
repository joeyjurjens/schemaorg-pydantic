from __future__ import annotations

from typing import ClassVar, Union

from pydantic import Field

from ..base import Date, DateTime, Text
from .creative_work import CreativeWork
from .series import Series

Date_DateTime = Union[Date, DateTime]

class CreativeWorkSeries(CreativeWork, Series):
    """A CreativeWorkSeries in schema.org is a group of related items, typically but not necessarily of the same kind. CreativeWorkSeries are usually organized into some order, often chronological. Unlike [[ItemList]] which is a general purpose data structure for lists of things, the emphasis with CreativeWorkSeries is on published materials (written e.g. books and periodicals, or media such as TV, radio and games)."""
    schema_type: ClassVar[str] = "CreativeWorkSeries"
    end_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="endDate", serialization_alias="endDate")
    issn: Text | list[Text] | None = Field(default=None)
    start_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="startDate", serialization_alias="startDate")
