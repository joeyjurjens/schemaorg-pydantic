from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work_season import CreativeWorkSeason


class PodcastSeason(CreativeWorkSeason):
    """A single season of a podcast. Many podcasts do not break down into separate seasons. In that case, PodcastSeries should be used."""
    schema_type: ClassVar[str] = "PodcastSeason"
