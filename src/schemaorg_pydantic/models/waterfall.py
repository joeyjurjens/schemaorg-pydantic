from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .body_of_water import BodyOfWater


class Waterfall(BodyOfWater):
    """A waterfall, like Niagara."""
    schema_type: ClassVar[str] = "Waterfall"
