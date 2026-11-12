from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .performing_group import PerformingGroup


class TheaterGroup(PerformingGroup):
    """A theater group or company, for example, the Royal Shakespeare Company or Druid Theatre."""
    schema_type: ClassVar[str] = "TheaterGroup"
