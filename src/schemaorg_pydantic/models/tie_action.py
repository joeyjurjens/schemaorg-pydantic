from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .achieve_action import AchieveAction


class TieAction(AchieveAction):
    """The act of reaching a draw in a competitive activity."""
    schema_type: ClassVar[str] = "TieAction"
