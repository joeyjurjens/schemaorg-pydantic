from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .web_page import WebPage


class ProfilePage(WebPage):
    """Web page type: Profile page."""
    schema_type: ClassVar[str] = "ProfilePage"
