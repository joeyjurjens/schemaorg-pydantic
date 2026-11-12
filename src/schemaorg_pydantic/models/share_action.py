from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .communicate_action import CommunicateAction


class ShareAction(CommunicateAction):
    """The act of distributing content to people for their amusement or edification."""
    schema_type: ClassVar[str] = "ShareAction"
