from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work_season import CreativeWorkSeason


class RadioSeason(CreativeWorkSeason):
    """Season dedicated to radio broadcast and associated online delivery."""
    schema_type: ClassVar[str] = "RadioSeason"
