from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work import CreativeWork


class Sculpture(CreativeWork):
    """A piece of sculpture."""
    schema_type: ClassVar[str] = "Sculpture"
