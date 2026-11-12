from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .news_article import NewsArticle


class AnalysisNewsArticle(NewsArticle):
    """An AnalysisNewsArticle is a [[NewsArticle]] that, while based on factual reporting, incorporates the expertise of the author/producer, offering interpretations and conclusions."""
    schema_type: ClassVar[str] = "AnalysisNewsArticle"
