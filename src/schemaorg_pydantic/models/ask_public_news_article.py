from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .news_article import NewsArticle


class AskPublicNewsArticle(NewsArticle):
    """A [[NewsArticle]] expressing an open call by a [[NewsMediaOrganization]] asking the public for input, insights, clarifications, anecdotes, documentation, etc., on an issue, for reporting purposes."""
    schema_type: ClassVar[str] = "AskPublicNewsArticle"
