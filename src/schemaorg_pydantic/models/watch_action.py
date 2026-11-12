from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .consume_action import ConsumeAction


class WatchAction(ConsumeAction):
    """The act of consuming dynamic/moving visual content."""
    schema_type: ClassVar[str] = "WatchAction"
