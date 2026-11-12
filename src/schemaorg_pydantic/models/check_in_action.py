from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .communicate_action import CommunicateAction


class CheckInAction(CommunicateAction):
    """The act of an agent communicating (service provider, social media, etc) their arrival by registering/confirming for a previously reserved service (e.g. flight check-in) or at a place (e.g. hotel), possibly resulting in a result (boarding pass, etc)."""
    schema_type: ClassVar[str] = "CheckInAction"
