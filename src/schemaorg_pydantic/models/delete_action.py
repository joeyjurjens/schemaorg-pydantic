from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .update_action import UpdateAction


class DeleteAction(UpdateAction):
    """The act of editing a recipient by removing one of its objects."""
    schema_type: ClassVar[str] = "DeleteAction"
