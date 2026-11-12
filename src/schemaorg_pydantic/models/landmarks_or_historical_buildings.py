from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .place import Place


class LandmarksOrHistoricalBuildings(Place):
    """An historical landmark or building."""
    schema_type: ClassVar[str] = "LandmarksOrHistoricalBuildings"
