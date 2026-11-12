from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .web_page import WebPage


class CollectionPage(WebPage):
    """Web page type: Collection page."""
    schema_type: ClassVar[str] = "CollectionPage"
