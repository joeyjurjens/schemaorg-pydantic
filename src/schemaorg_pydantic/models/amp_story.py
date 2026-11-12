from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .media_object import MediaObject


class AmpStory(MediaObject):
    """A creative work with a visual storytelling format intended to be viewed online, particularly on mobile devices."""
    schema_type: ClassVar[str] = "AmpStory"
