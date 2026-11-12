from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .sports_activity_location import SportsActivityLocation


class PublicSwimmingPool(SportsActivityLocation):
    """A public swimming pool."""
    schema_type: ClassVar[str] = "PublicSwimmingPool"
