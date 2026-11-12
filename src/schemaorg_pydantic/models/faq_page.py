from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .web_page import WebPage


class FAQPage(WebPage):
    """A [[FAQPage]] is a [[WebPage]] presenting one or more \"[Frequently asked questions](https://en.wikipedia.org/wiki/FAQ)\" (see also [[QAPage]])."""
    schema_type: ClassVar[str] = "FAQPage"
