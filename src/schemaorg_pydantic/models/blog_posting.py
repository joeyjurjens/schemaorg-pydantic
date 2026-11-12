from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .social_media_posting import SocialMediaPosting


class BlogPosting(SocialMediaPosting):
    """A blog post."""
    schema_type: ClassVar[str] = "BlogPosting"
