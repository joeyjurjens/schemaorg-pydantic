from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .news_article import NewsArticle


class ReportageNewsArticle(NewsArticle):
    """The [[ReportageNewsArticle]] type is a subtype of [[NewsArticle]] representing\n news articles which are the result of journalistic news reporting conventions."""
    schema_type: ClassVar[str] = "ReportageNewsArticle"
