from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .category_code import CategoryCode
from .medical_intangible import MedicalIntangible


class MedicalCode(CategoryCode, MedicalIntangible):
    """A code for a medical entity."""
    schema_type: ClassVar[str] = "MedicalCode"
    coding_system: Text | list[Text] | None = Field(default=None, validation_alias="codingSystem", serialization_alias="codingSystem")
