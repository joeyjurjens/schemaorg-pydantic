from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work import CreativeWork


class Atlas(CreativeWork):
    """A collection or bound volume of maps, charts, plates or tables, physical or in media form illustrating any subject."""
    schema_type: ClassVar[str] = "Atlas"
