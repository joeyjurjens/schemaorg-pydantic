from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .web_page_element import WebPageElement


class Table(WebPageElement):
    """A table on a Web page."""
    schema_type: ClassVar[str] = "Table"
