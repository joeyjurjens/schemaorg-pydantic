from __future__ import annotations

from typing import ClassVar, Union

from pydantic import Field

from ..base import Integer, Text
from .creative_work import CreativeWork

Integer_Text = Union[Integer, Text]

class PublicationIssue(CreativeWork):
    """A part of a successively published publication such as a periodical or publication volume, often numbered, usually containing a grouping of works such as articles."""
    schema_type: ClassVar[str] = "PublicationIssue"
    issue_number: Integer_Text | list[Integer_Text] | None = Field(default=None, validation_alias="issueNumber", serialization_alias="issueNumber")
    page_end: Integer_Text | list[Integer_Text] | None = Field(default=None, validation_alias="pageEnd", serialization_alias="pageEnd")
    page_start: Integer_Text | list[Integer_Text] | None = Field(default=None, validation_alias="pageStart", serialization_alias="pageStart")
    pagination: Text | list[Text] | None = Field(default=None)
