from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .assess_action import AssessAction


class ReactAction(AssessAction):
    """The act of responding instinctively and emotionally to an object, expressing a sentiment."""
    schema_type: ClassVar[str] = "ReactAction"
