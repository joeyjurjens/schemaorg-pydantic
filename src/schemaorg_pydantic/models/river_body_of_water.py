from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .body_of_water import BodyOfWater


class RiverBodyOfWater(BodyOfWater):
    """A river (for example, the broad majestic Shannon)."""
    schema_type: ClassVar[str] = "RiverBodyOfWater"
