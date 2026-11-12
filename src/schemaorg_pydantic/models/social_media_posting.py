from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .article import Article

if TYPE_CHECKING:
    from .creative_work import CreativeWork

if TYPE_CHECKING:
    CreativeWork_Ref = Union[CreativeWork, Ref]
else:
    CreativeWork_Ref = Union[Is["CreativeWork"], Ref]


class SocialMediaPosting(Article):
    """A post to a social media platform, including blog posts, tweets, Facebook posts, etc."""
    schema_type: ClassVar[str] = "SocialMediaPosting"
    shared_content: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="sharedContent", serialization_alias="sharedContent")
