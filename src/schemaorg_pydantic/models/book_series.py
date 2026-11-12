from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work_series import CreativeWorkSeries


class BookSeries(CreativeWorkSeries):
    """A series of books. Included books can be indicated with the hasPart property."""
    schema_type: ClassVar[str] = "BookSeries"
