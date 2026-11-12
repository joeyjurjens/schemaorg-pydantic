from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .blog_posting import BlogPosting

if TYPE_CHECKING:
    BlogPosting_Ref = Union[BlogPosting, Ref]
else:
    BlogPosting_Ref = Union[Is["BlogPosting"], Ref]


class Blog(CreativeWork):
    """A [blog](https://en.wikipedia.org/wiki/Blog), sometimes known as a \"weblog\". Note that the individual posts ([[BlogPosting]]s) in a [[Blog]] are often colloquially referred to by the same term."""
    schema_type: ClassVar[str] = "Blog"
    blog_post: BlogPosting_Ref | list[BlogPosting_Ref] | None = Field(default=None, validation_alias="blogPost", serialization_alias="blogPost")
    issn: Text | list[Text] | None = Field(default=None)
