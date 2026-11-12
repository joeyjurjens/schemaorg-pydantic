from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .action import Action


class ControlAction(Action):
    """An agent controls a device or application."""
    schema_type: ClassVar[str] = "ControlAction"
