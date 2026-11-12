from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .allocate_action import AllocateAction


class AcceptAction(AllocateAction):
    """The act of committing to/adopting an object."""
    schema_type: ClassVar[str] = "AcceptAction"
