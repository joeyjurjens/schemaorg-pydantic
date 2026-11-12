from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .clip import Clip


class VideoGameClip(Clip):
    """A short segment/part of a video game."""
    schema_type: ClassVar[str] = "VideoGameClip"
