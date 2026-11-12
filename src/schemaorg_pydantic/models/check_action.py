from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .find_action import FindAction


class CheckAction(FindAction):
    """An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state."""
    schema_type: ClassVar[str] = "CheckAction"
