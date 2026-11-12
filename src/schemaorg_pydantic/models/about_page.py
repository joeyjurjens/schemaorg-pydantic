from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .web_page import WebPage


class AboutPage(WebPage):
    """Web page type: About page."""
    schema_type: ClassVar[str] = "AboutPage"
