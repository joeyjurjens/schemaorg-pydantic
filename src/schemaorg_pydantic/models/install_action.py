from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .consume_action import ConsumeAction


class InstallAction(ConsumeAction):
    """The act of installing an application."""
    schema_type: ClassVar[str] = "InstallAction"
