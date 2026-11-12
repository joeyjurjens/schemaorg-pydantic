from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .digital_document import DigitalDocument


class PresentationDigitalDocument(DigitalDocument):
    """A file containing slides or used for a presentation."""
    schema_type: ClassVar[str] = "PresentationDigitalDocument"
