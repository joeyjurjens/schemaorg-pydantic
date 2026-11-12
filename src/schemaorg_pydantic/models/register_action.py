from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .interact_action import InteractAction


class RegisterAction(InteractAction):
    """The act of registering to be a user of a service, product or web page."""
    schema_type: ClassVar[str] = "RegisterAction"
