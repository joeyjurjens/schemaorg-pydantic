from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .software_application import SoftwareApplication


class WebApplication(SoftwareApplication):
    """Web applications."""
    schema_type: ClassVar[str] = "WebApplication"
    browser_requirements: Text | list[Text] | None = Field(default=None, validation_alias="browserRequirements", serialization_alias="browserRequirements")
