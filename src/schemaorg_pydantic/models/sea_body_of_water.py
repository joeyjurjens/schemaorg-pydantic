from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .body_of_water import BodyOfWater


class SeaBodyOfWater(BodyOfWater):
    """A sea (for example, the Caspian sea)."""
    schema_type: ClassVar[str] = "SeaBodyOfWater"
