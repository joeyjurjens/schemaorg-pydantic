from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .action import Action


class AssessAction(Action):
    """The act of forming one's opinion, reaction or sentiment."""
    schema_type: ClassVar[str] = "AssessAction"
