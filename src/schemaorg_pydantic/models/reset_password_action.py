from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .control_action import ControlAction


class ResetPasswordAction(ControlAction):
    """The action of resetting the password of a device or application."""
    schema_type: ClassVar[str] = "ResetPasswordAction"
