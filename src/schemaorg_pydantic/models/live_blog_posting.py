from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import DateTime, Is, Ref
from .blog_posting import BlogPosting

if TYPE_CHECKING:
    BlogPosting_Ref = Union[BlogPosting, Ref]
else:
    BlogPosting_Ref = Union[Is["BlogPosting"], Ref]


class LiveBlogPosting(BlogPosting):
    """A [[LiveBlogPosting]] is a [[BlogPosting]] intended to provide a rolling textual coverage of an ongoing event through continuous updates."""
    schema_type: ClassVar[str] = "LiveBlogPosting"
    coverage_end_time: DateTime | list[DateTime] | None = Field(default=None, validation_alias="coverageEndTime", serialization_alias="coverageEndTime")
    coverage_start_time: DateTime | list[DateTime] | None = Field(default=None, validation_alias="coverageStartTime", serialization_alias="coverageStartTime")
    live_blog_update: BlogPosting_Ref | list[BlogPosting_Ref] | None = Field(default=None, validation_alias="liveBlogUpdate", serialization_alias="liveBlogUpdate")
