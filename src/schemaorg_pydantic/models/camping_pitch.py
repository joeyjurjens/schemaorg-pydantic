from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .accommodation import Accommodation


class CampingPitch(Accommodation):
    """A [[CampingPitch]] is an individual place for overnight stay in the outdoors, typically being part of a larger camping site, or [[Campground]]."""
    schema_type: ClassVar[str] = "CampingPitch"
