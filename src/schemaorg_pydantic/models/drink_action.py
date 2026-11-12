from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .consume_action import ConsumeAction


class DrinkAction(ConsumeAction):
    """The act of swallowing liquids."""
    schema_type: ClassVar[str] = "DrinkAction"
