from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .allocate_action import AllocateAction


class RejectAction(AllocateAction):
    """The act of rejecting to/adopting an object."""
    schema_type: ClassVar[str] = "RejectAction"
