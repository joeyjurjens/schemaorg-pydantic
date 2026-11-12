from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .article import Article


class ScholarlyArticle(Article):
    """A scholarly article."""
    schema_type: ClassVar[str] = "ScholarlyArticle"
