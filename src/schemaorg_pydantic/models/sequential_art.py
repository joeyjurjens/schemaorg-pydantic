from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .book import Book
from .visual_artwork import VisualArtwork


class SequentialArt(Book, VisualArtwork):
    """An art forms that use images deployed in a specific order for the purpose of graphic storytelling (i.e., narration of graphic stories) or conveying information. Examples of SequentialArt are Franco-Belgian Bande Dessin\u00e9e, Comics in the USA and \u6f2b\u753b (Manga) in Japan."""
    schema_type: ClassVar[str] = "SequentialArt"
