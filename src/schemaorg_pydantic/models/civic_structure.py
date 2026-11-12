from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .place import Place


class CivicStructure(Place):
    """A public structure, such as a town hall or concert hall."""
    schema_type: ClassVar[str] = "CivicStructure"
    opening_hours: Text | list[Text] | None = Field(default=None, validation_alias="openingHours", serialization_alias="openingHours")
