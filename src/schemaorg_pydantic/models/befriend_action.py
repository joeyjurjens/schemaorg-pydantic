from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .interact_action import InteractAction


class BefriendAction(InteractAction):
    """The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically."""
    schema_type: ClassVar[str] = "BefriendAction"
