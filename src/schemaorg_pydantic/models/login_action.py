from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .control_action import ControlAction


class LoginAction(ControlAction):
    """The action of logging into a device or application."""
    schema_type: ClassVar[str] = "LoginAction"
