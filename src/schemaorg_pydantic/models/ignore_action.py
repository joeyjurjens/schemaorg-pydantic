from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .assess_action import AssessAction


class IgnoreAction(AssessAction):
    """The act of intentionally disregarding the object. An agent ignores an object."""
    schema_type: ClassVar[str] = "IgnoreAction"
