from __future__ import annotations

from typing import ClassVar, Union

from pydantic import Field

from ..base import Date, DateTime
from .organize_action import OrganizeAction

Date_DateTime = Union[Date, DateTime]

class PlanAction(OrganizeAction):
    """The act of planning the execution of an event/task/action/reservation/plan to a future date."""
    schema_type: ClassVar[str] = "PlanAction"
    scheduled_time: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="scheduledTime", serialization_alias="scheduledTime")
