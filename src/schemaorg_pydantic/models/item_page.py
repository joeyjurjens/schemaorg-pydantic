from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .web_page import WebPage


class ItemPage(WebPage):
    """A page devoted to a single item, such as a particular product or hotel."""
    schema_type: ClassVar[str] = "ItemPage"
