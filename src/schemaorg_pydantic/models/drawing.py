from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work import CreativeWork


class Drawing(CreativeWork):
    """A picture or diagram made with a pencil, pen, or crayon rather than paint."""
    schema_type: ClassVar[str] = "Drawing"
