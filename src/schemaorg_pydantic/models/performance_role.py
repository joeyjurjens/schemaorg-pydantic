from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .role import Role


class PerformanceRole(Role):
    """A PerformanceRole is a Role that some entity places with regard to a theatrical performance, e.g. in a Movie, TVSeries etc."""
    schema_type: ClassVar[str] = "PerformanceRole"
    character_name: Text | list[Text] | None = Field(default=None, validation_alias="characterName", serialization_alias="characterName")
