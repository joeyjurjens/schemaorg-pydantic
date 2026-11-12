from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref
from .creative_work import CreativeWork

if TYPE_CHECKING:
    Comment_CreativeWork_Ref = Union["Comment", CreativeWork, Ref]
else:
    Comment_CreativeWork_Ref = Union[Is["Comment"], Is["CreativeWork"], Ref]

if TYPE_CHECKING:
    CreativeWork_Ref = Union[CreativeWork, Ref]
else:
    CreativeWork_Ref = Union[Is["CreativeWork"], Ref]


class Comment(CreativeWork):
    """A comment on an item - for example, a comment on a blog post. The comment's content is expressed via the [[text]] property, and its topic via [[about]], properties shared with all CreativeWorks."""
    schema_type: ClassVar[str] = "Comment"
    downvote_count: Integer | list[Integer] | None = Field(default=None, validation_alias="downvoteCount", serialization_alias="downvoteCount")
    parent_item: Comment_CreativeWork_Ref | list[Comment_CreativeWork_Ref] | None = Field(default=None, validation_alias="parentItem", serialization_alias="parentItem")
    shared_content: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="sharedContent", serialization_alias="sharedContent")
    upvote_count: Integer | list[Integer] | None = Field(default=None, validation_alias="upvoteCount", serialization_alias="upvoteCount")
