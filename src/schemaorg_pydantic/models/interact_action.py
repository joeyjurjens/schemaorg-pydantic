from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .action import Action


class InteractAction(Action):
    """The act of interacting with another person or organization."""
    schema_type: ClassVar[str] = "InteractAction"
