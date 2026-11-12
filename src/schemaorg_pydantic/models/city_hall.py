from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .government_building import GovernmentBuilding


class CityHall(GovernmentBuilding):
    """A city hall."""
    schema_type: ClassVar[str] = "CityHall"
