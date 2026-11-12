from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .control_action import ControlAction


class ActivateAction(ControlAction):
    """The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight)."""
    schema_type: ClassVar[str] = "ActivateAction"
