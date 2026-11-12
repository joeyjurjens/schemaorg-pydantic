from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .inform_action import InformAction


class ConfirmAction(InformAction):
    """The act of notifying someone that a future event/action is going to happen as expected."""
    schema_type: ClassVar[str] = "ConfirmAction"
