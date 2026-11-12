from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .digital_document import DigitalDocument


class TextDigitalDocument(DigitalDocument):
    """A file composed primarily of text."""
    schema_type: ClassVar[str] = "TextDigitalDocument"
