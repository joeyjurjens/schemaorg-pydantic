from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .article import Article


class AdvertiserContentArticle(Article):
    """An [[Article]] that an external entity has paid to place or to produce to its specifications. Includes [advertorials](https://en.wikipedia.org/wiki/Advertorial), sponsored content, native advertising and other paid content."""
    schema_type: ClassVar[str] = "AdvertiserContentArticle"
