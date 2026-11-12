from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .creative_work import CreativeWork


class WebSite(CreativeWork):
    """A WebSite is a set of related web pages and other items typically served from a single web domain and accessible via URLs."""
    schema_type: ClassVar[str] = "WebSite"
    issn: Text | list[Text] | None = Field(default=None)
