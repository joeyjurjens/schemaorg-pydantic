from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work import CreativeWork


class Photograph(CreativeWork):
    """A photograph."""
    schema_type: ClassVar[str] = "Photograph"
