from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .control_action import ControlAction


class ResumeAction(ControlAction):
    """The act of resuming a device or application which was formerly paused (e.g. resume music playback or resume a timer)."""
    schema_type: ClassVar[str] = "ResumeAction"
