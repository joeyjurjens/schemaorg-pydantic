from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .interact_action import InteractAction


class SubscribeAction(InteractAction):
    """The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates pushed to."""
    schema_type: ClassVar[str] = "SubscribeAction"
