from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .digital_document import DigitalDocument


class NoteDigitalDocument(DigitalDocument):
    """A file containing a note, primarily for the author."""
    schema_type: ClassVar[str] = "NoteDigitalDocument"
