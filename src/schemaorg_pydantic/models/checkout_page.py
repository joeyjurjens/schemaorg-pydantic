from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .web_page import WebPage


class CheckoutPage(WebPage):
    """Web page type: Checkout page."""
    schema_type: ClassVar[str] = "CheckoutPage"
