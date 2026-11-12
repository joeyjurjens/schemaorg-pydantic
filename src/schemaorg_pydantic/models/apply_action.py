from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organize_action import OrganizeAction


class ApplyAction(OrganizeAction):
    """The act of registering to an organization/service without the guarantee to receive it."""
    schema_type: ClassVar[str] = "ApplyAction"
