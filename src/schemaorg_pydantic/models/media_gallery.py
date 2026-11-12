from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .collection_page import CollectionPage


class MediaGallery(CollectionPage):
    """Web page type: Media gallery page. A mixed-media page that can contain media such as images, videos, and other multimedia."""
    schema_type: ClassVar[str] = "MediaGallery"
