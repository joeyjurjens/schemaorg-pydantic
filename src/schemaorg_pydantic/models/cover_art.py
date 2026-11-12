from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .visual_artwork import VisualArtwork


class CoverArt(VisualArtwork):
    """The artwork on the outer surface of a CreativeWork."""
    schema_type: ClassVar[str] = "CoverArt"
