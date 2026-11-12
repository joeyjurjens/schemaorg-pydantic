from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .comic_story import ComicStory
from .cover_art import CoverArt


class ComicCoverArt(ComicStory, CoverArt):
    """The artwork on the cover of a comic."""
    schema_type: ClassVar[str] = "ComicCoverArt"
