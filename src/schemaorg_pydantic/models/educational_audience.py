from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .audience import Audience


class EducationalAudience(Audience):
    """An EducationalAudience."""
    schema_type: ClassVar[str] = "EducationalAudience"
    educational_role: Text | list[Text] | None = Field(default=None, validation_alias="educationalRole", serialization_alias="educationalRole")
