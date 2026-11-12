from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .health_and_beauty_business import HealthAndBeautyBusiness
from .sports_activity_location import SportsActivityLocation


class HealthClub(HealthAndBeautyBusiness, SportsActivityLocation):
    """A health club."""
    schema_type: ClassVar[str] = "HealthClub"
