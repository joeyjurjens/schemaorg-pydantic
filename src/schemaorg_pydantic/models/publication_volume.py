from __future__ import annotations

from typing import ClassVar, Union

from pydantic import Field

from ..base import Integer, Text
from .creative_work import CreativeWork

Integer_Text = Union[Integer, Text]

class PublicationVolume(CreativeWork):
    """A part of a successively published publication such as a periodical or multi-volume work, often numbered. It may represent a time span, such as a year."""
    schema_type: ClassVar[str] = "PublicationVolume"
    page_end: Integer_Text | list[Integer_Text] | None = Field(default=None, validation_alias="pageEnd", serialization_alias="pageEnd")
    page_start: Integer_Text | list[Integer_Text] | None = Field(default=None, validation_alias="pageStart", serialization_alias="pageStart")
    pagination: Text | list[Text] | None = Field(default=None)
    volume_number: Integer_Text | list[Integer_Text] | None = Field(default=None, validation_alias="volumeNumber", serialization_alias="volumeNumber")
