from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .social_media_posting import SocialMediaPosting


class DiscussionForumPosting(SocialMediaPosting):
    """A posting to a discussion forum."""
    schema_type: ClassVar[str] = "DiscussionForumPosting"
