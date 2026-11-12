from __future__ import annotations

from typing import ClassVar, Union

from pydantic import Field

from ..base import Integer, Text
from .creative_work import CreativeWork

Integer_Text = Union[Integer, Text]

class Chapter(CreativeWork):
    """One of the sections into which a book is divided. A chapter usually has a section number or a name."""
    schema_type: ClassVar[str] = "Chapter"
    page_end: Integer_Text | list[Integer_Text] | None = Field(default=None, validation_alias="pageEnd", serialization_alias="pageEnd")
    page_start: Integer_Text | list[Integer_Text] | None = Field(default=None, validation_alias="pageStart", serialization_alias="pageStart")
    pagination: Text | list[Text] | None = Field(default=None)
