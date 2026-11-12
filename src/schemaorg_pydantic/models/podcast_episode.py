from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .episode import Episode


class PodcastEpisode(Episode):
    """A single episode of a podcast series."""
    schema_type: ClassVar[str] = "PodcastEpisode"
