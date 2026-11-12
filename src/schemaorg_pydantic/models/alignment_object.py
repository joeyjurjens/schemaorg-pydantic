from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text, Url
from .intangible import Intangible


class AlignmentObject(Intangible):
    """An intangible item that describes an alignment between a learning resource and a node in an educational framework.\nShould not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency."""
    schema_type: ClassVar[str] = "AlignmentObject"
    alignment_type: Text | list[Text] | None = Field(default=None, validation_alias="alignmentType", serialization_alias="alignmentType")
    educational_framework: Text | list[Text] | None = Field(default=None, validation_alias="educationalFramework", serialization_alias="educationalFramework")
    target_description: Text | list[Text] | None = Field(default=None, validation_alias="targetDescription", serialization_alias="targetDescription")
    target_name: Text | list[Text] | None = Field(default=None, validation_alias="targetName", serialization_alias="targetName")
    target_url: Url | list[Url] | None = Field(default=None, validation_alias="targetUrl", serialization_alias="targetUrl")
