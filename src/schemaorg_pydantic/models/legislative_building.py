from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .government_building import GovernmentBuilding


class LegislativeBuilding(GovernmentBuilding):
    """A legislative building&#x2014;for example, the state capitol."""
    schema_type: ClassVar[str] = "LegislativeBuilding"
