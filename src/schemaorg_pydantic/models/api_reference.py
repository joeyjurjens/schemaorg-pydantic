from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .tech_article import TechArticle


class APIReference(TechArticle):
    """Reference documentation for application programming interfaces (APIs)."""
    schema_type: ClassVar[str] = "APIReference"
    assembly_version: Text | list[Text] | None = Field(default=None, validation_alias="assemblyVersion", serialization_alias="assemblyVersion")
    executable_library_name: Text | list[Text] | None = Field(default=None, validation_alias="executableLibraryName", serialization_alias="executableLibraryName")
    programming_model: Text | list[Text] | None = Field(default=None, validation_alias="programmingModel", serialization_alias="programmingModel")
    target_platform: Text | list[Text] | None = Field(default=None, validation_alias="targetPlatform", serialization_alias="targetPlatform")
