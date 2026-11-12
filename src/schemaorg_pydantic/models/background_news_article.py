from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .news_article import NewsArticle


class BackgroundNewsArticle(NewsArticle):
    """A [[NewsArticle]] providing historical context, definition and detail on a specific topic (aka \"explainer\" or \"backgrounder\"). For example, an in-depth article or frequently-asked-questions ([FAQ](https://en.wikipedia.org/wiki/FAQ)) document on topics such as Climate Change or the European Union. Other kinds of background material from a non-news setting are often described using [[Book]] or [[Article]], in particular [[ScholarlyArticle]]. See also [[NewsArticle]] for related vocabulary from a learning/education perspective."""
    schema_type: ClassVar[str] = "BackgroundNewsArticle"
