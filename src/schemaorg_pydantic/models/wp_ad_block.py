from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .web_page_element import WebPageElement


class WPAdBlock(WebPageElement):
    """An advertising section of the page."""
    schema_type: ClassVar[str] = "WPAdBlock"
