from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .body_of_water import BodyOfWater


class OceanBodyOfWater(BodyOfWater):
    """An ocean (for example, the Pacific)."""
    schema_type: ClassVar[str] = "OceanBodyOfWater"
