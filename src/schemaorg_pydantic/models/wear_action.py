from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .use_action import UseAction


class WearAction(UseAction):
    """The act of dressing oneself in clothing."""
    schema_type: ClassVar[str] = "WearAction"
