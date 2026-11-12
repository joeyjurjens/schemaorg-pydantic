from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work import CreativeWork


class Manuscript(CreativeWork):
    """A book, document, or piece of music written by hand rather than typed or printed."""
    schema_type: ClassVar[str] = "Manuscript"
