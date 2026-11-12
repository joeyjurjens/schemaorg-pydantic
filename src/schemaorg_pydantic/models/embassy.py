from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .government_building import GovernmentBuilding


class Embassy(GovernmentBuilding):
    """An embassy."""
    schema_type: ClassVar[str] = "Embassy"
