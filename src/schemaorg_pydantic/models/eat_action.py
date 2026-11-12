from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .consume_action import ConsumeAction


class EatAction(ConsumeAction):
    """The act of swallowing solid objects."""
    schema_type: ClassVar[str] = "EatAction"
