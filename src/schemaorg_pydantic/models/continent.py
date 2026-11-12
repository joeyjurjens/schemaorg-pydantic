from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .landform import Landform


class Continent(Landform):
    """One of the continents (for example, Europe or Africa)."""
    schema_type: ClassVar[str] = "Continent"
