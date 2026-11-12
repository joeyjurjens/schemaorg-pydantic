from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .intangible import Intangible


class Series(Intangible):
    """A Series in schema.org is a group of related items, typically but not necessarily of the same kind. See also [[CreativeWorkSeries]], [[EventSeries]]."""
    schema_type: ClassVar[str] = "Series"
