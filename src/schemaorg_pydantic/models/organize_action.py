from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .action import Action


class OrganizeAction(Action):
    """The act of manipulating/administering/supervising/controlling one or more objects."""
    schema_type: ClassVar[str] = "OrganizeAction"
