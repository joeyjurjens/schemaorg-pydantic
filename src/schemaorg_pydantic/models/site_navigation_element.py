from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .web_page_element import WebPageElement


class SiteNavigationElement(WebPageElement):
    """A navigation element of the page."""
    schema_type: ClassVar[str] = "SiteNavigationElement"
