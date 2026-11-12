from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .media_object import MediaObject


class TextObject(MediaObject):
    """A text file. The text can be unformatted or contain markup, html, etc."""
    schema_type: ClassVar[str] = "TextObject"
