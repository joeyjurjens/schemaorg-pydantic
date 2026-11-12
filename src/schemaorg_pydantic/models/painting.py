from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work import CreativeWork


class Painting(CreativeWork):
    """A painting."""
    schema_type: ClassVar[str] = "Painting"
