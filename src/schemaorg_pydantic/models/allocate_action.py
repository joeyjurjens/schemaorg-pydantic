from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organize_action import OrganizeAction


class AllocateAction(OrganizeAction):
    """The act of organizing tasks/objects/events by associating resources to it."""
    schema_type: ClassVar[str] = "AllocateAction"
