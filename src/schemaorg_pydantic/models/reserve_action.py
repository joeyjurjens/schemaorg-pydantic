from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .plan_action import PlanAction


class ReserveAction(PlanAction):
    """Reserving a concrete object."""
    schema_type: ClassVar[str] = "ReserveAction"
