from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .body_of_water import BodyOfWater


class Reservoir(BodyOfWater):
    """A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir."""
    schema_type: ClassVar[str] = "Reservoir"
