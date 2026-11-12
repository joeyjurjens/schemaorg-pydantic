from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .body_of_water import BodyOfWater


class LakeBodyOfWater(BodyOfWater):
    """A lake (for example, Lake Pontrachain)."""
    schema_type: ClassVar[str] = "LakeBodyOfWater"
