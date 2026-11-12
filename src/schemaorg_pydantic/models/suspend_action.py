from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .control_action import ControlAction


class SuspendAction(ControlAction):
    """The act of momentarily pausing a device or application (e.g. pause music playback or pause a timer)."""
    schema_type: ClassVar[str] = "SuspendAction"
