from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .media_gallery import MediaGallery


class ImageGallery(MediaGallery):
    """Web page type: Image gallery page."""
    schema_type: ClassVar[str] = "ImageGallery"
