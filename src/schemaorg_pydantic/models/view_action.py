from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .consume_action import ConsumeAction


class ViewAction(ConsumeAction):
    """The act of consuming static visual content."""
    schema_type: ClassVar[str] = "ViewAction"
