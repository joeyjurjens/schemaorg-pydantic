from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .landform import Landform


class Volcano(Landform):
    """A volcano, like Fujisan."""
    schema_type: ClassVar[str] = "Volcano"
