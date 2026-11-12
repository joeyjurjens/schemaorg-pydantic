from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .performing_group import PerformingGroup


class DanceGroup(PerformingGroup):
    """A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance."""
    schema_type: ClassVar[str] = "DanceGroup"
