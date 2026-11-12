from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure
from .lodging_business import LodgingBusiness


class Campground(CivicStructure, LodgingBusiness):
    """A camping site, campsite, or [[Campground]] is a place used for overnight stay in the outdoors, typically containing individual [[CampingPitch]] locations."""
    schema_type: ClassVar[str] = "Campground"
