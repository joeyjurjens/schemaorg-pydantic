from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .web_page import WebPage


class SearchResultsPage(WebPage):
    """Web page type: Search results page."""
    schema_type: ClassVar[str] = "SearchResultsPage"
