from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .landform import Landform


class BodyOfWater(Landform):
    """A body of water, such as a sea, ocean, or lake."""
    schema_type: ClassVar[str] = "BodyOfWater"
