from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .communicate_action import CommunicateAction


class CheckOutAction(CommunicateAction):
    """The act of an agent communicating (service provider, social media, etc) their departure of a previously reserved service (e.g. flight check-in) or place (e.g. hotel)."""
    schema_type: ClassVar[str] = "CheckOutAction"
