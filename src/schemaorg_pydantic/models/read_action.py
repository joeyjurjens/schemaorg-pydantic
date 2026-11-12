from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .consume_action import ConsumeAction


class ReadAction(ConsumeAction):
    """The act of consuming written content."""
    schema_type: ClassVar[str] = "ReadAction"
