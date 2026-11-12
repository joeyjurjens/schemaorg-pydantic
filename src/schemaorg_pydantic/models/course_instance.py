from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .event import Event

if TYPE_CHECKING:
    from .person import Person
    from .schedule import Schedule

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]

if TYPE_CHECKING:
    Schedule_Ref = Union[Schedule, Ref]
else:
    Schedule_Ref = Union[Is["Schedule"], Ref]


class CourseInstance(Event):
    """An instance of a [[Course]] which is distinct from other instances because it is offered at a different time or location or through different media or modes of study or to a specific section of students."""
    schema_type: ClassVar[str] = "CourseInstance"
    course_mode: Text | list[Text] | None = Field(default=None, validation_alias="courseMode", serialization_alias="courseMode")
    course_schedule: Schedule_Ref | list[Schedule_Ref] | None = Field(default=None, validation_alias="courseSchedule", serialization_alias="courseSchedule")
    course_workload: Text | list[Text] | None = Field(default=None, validation_alias="courseWorkload", serialization_alias="courseWorkload")
    instructor: Person_Ref | list[Person_Ref] | None = Field(default=None)
