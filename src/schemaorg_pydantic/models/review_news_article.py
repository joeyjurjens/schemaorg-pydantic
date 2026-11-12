from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .critic_review import CriticReview
from .news_article import NewsArticle


class ReviewNewsArticle(CriticReview, NewsArticle):
    """A [[NewsArticle]] and [[CriticReview]] providing a professional critic's assessment of a service, product, performance, or artistic or literary work."""
    schema_type: ClassVar[str] = "ReviewNewsArticle"
