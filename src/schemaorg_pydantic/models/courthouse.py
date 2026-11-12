from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .government_building import GovernmentBuilding


class Courthouse(GovernmentBuilding):
    """A courthouse."""
    schema_type: ClassVar[str] = "Courthouse"
