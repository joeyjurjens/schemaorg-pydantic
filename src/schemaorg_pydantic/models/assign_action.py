from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .allocate_action import AllocateAction


class AssignAction(AllocateAction):
    """The act of allocating an action/event/task to some destination (someone or something)."""
    schema_type: ClassVar[str] = "AssignAction"
