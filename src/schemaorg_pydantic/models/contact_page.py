from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .web_page import WebPage


class ContactPage(WebPage):
    """Web page type: Contact page."""
    schema_type: ClassVar[str] = "ContactPage"
