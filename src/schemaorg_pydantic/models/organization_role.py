from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Number
from .role import Role


class OrganizationRole(Role):
    """A subclass of Role used to describe roles within organizations."""
    schema_type: ClassVar[str] = "OrganizationRole"
    numbered_position: Number | list[Number] | None = Field(default=None, validation_alias="numberedPosition", serialization_alias="numberedPosition")
