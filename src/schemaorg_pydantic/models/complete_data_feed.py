from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .data_feed import DataFeed


class CompleteDataFeed(DataFeed):
    """A [[CompleteDataFeed]] is a [[DataFeed]] whose standard representation includes content for every item currently in the feed."""
    schema_type: ClassVar[str] = "CompleteDataFeed"
