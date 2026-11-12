from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .consume_action import ConsumeAction


class ListenAction(ConsumeAction):
    """The act of consuming audio content."""
    schema_type: ClassVar[str] = "ListenAction"
