from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .creative_work_season import CreativeWorkSeason


class TVSeason(CreativeWorkSeason):
    """Season dedicated to TV broadcast and associated online delivery."""
    schema_type: ClassVar[str] = "TVSeason"
    title_eidr: Text | list[Text] | None = Field(default=None, validation_alias="titleEIDR", serialization_alias="titleEIDR")
