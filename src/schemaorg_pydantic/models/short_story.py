from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work import CreativeWork


class ShortStory(CreativeWork):
    """Short story or tale. A brief work of literature, usually written in narrative prose."""
    schema_type: ClassVar[str] = "ShortStory"
