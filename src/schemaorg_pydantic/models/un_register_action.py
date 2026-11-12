from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .interact_action import InteractAction


class UnRegisterAction(InteractAction):
    """The act of un-registering from a service."""
    schema_type: ClassVar[str] = "UnRegisterAction"
