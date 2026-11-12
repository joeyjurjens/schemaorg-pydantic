from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .media_object import MediaObject


class MusicVideoObject(MediaObject):
    """A music video file."""
    schema_type: ClassVar[str] = "MusicVideoObject"
