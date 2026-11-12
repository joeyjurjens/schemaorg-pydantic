from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .consume_action import ConsumeAction


class UseAction(ConsumeAction):
    """The act of applying an object to its intended purpose."""
    schema_type: ClassVar[str] = "UseAction"
