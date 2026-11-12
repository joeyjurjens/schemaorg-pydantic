from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .body_of_water import BodyOfWater


class Canal(BodyOfWater):
    """A canal, like the Panama Canal."""
    schema_type: ClassVar[str] = "Canal"
