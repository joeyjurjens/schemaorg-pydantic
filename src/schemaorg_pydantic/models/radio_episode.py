from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .episode import Episode


class RadioEpisode(Episode):
    """A radio episode which can be part of a series or season."""
    schema_type: ClassVar[str] = "RadioEpisode"
