from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .article import Article


class SatiricalArticle(Article):
    """An [[Article]] whose content is primarily [[satirical]](https://en.wikipedia.org/wiki/Satire) in nature, i.e. unlikely to be literally true. A satirical article is sometimes but not necessarily also a [[NewsArticle]]. [[ScholarlyArticle]]s are also sometimes satirized."""
    schema_type: ClassVar[str] = "SatiricalArticle"
