from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .plan_action import PlanAction


class ScheduleAction(PlanAction):
    """Scheduling future actions, events, or tasks."""
    schema_type: ClassVar[str] = "ScheduleAction"
