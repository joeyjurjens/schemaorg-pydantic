from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .interact_action import InteractAction


class MarryAction(InteractAction):
    """The act of marrying a person."""
    schema_type: ClassVar[str] = "MarryAction"
