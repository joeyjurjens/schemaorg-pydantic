from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .media_gallery import MediaGallery


class VideoGallery(MediaGallery):
    """Web page type: Video gallery page."""
    schema_type: ClassVar[str] = "VideoGallery"
