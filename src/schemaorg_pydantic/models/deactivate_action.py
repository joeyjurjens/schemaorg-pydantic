from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .control_action import ControlAction


class DeactivateAction(ControlAction):
    """The act of stopping or deactivating a device or application (e.g. stopping a timer or turning off a flashlight)."""
    schema_type: ClassVar[str] = "DeactivateAction"
