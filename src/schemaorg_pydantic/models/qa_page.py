from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .web_page import WebPage


class QAPage(WebPage):
    """A QAPage is a WebPage focussed on a specific Question and its Answer(s), e.g. in a question answering site or documenting Frequently Asked Questions (FAQs)."""
    schema_type: ClassVar[str] = "QAPage"
