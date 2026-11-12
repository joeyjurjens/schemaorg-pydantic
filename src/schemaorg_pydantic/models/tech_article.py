from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .article import Article


class TechArticle(Article):
    """A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc."""
    schema_type: ClassVar[str] = "TechArticle"
    dependencies: Text | list[Text] | None = Field(default=None)
    proficiency_level: Text | list[Text] | None = Field(default=None, validation_alias="proficiencyLevel", serialization_alias="proficiencyLevel")
