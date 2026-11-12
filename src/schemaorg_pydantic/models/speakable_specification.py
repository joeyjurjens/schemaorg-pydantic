from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .intangible import Intangible


class SpeakableSpecification(Intangible):
    """A SpeakableSpecification indicates (typically via [[xpath]] or [[cssSelector]]) sections of a document that are highlighted as particularly [[speakable]]. Instances of this type are expected to be used primarily as values of the [[speakable]] property."""
    schema_type: ClassVar[str] = "SpeakableSpecification"
    css_selector: Text | list[Text] | None = Field(default=None, validation_alias="cssSelector", serialization_alias="cssSelector")
    xpath: Text | list[Text] | None = Field(default=None)
