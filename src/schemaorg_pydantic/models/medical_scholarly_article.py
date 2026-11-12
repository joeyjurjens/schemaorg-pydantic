from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .scholarly_article import ScholarlyArticle


class MedicalScholarlyArticle(ScholarlyArticle):
    """A scholarly article in the medical domain."""
    schema_type: ClassVar[str] = "MedicalScholarlyArticle"
    publication_type: Text | list[Text] | None = Field(default=None, validation_alias="publicationType", serialization_alias="publicationType")
