from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .creative_work import CreativeWork


class WebPageElement(CreativeWork):
    """A web page element, like a table or an image."""
    schema_type: ClassVar[str] = "WebPageElement"
    css_selector: Text | list[Text] | None = Field(default=None, validation_alias="cssSelector", serialization_alias="cssSelector")
    xpath: Text | list[Text] | None = Field(default=None)
