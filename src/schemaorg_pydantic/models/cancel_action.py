from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .plan_action import PlanAction


class CancelAction(PlanAction):
    """The act of asserting that a future event/action is no longer going to happen."""
    schema_type: ClassVar[str] = "CancelAction"
