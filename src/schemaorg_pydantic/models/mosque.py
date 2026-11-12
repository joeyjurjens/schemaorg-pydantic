from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .place_of_worship import PlaceOfWorship


class Mosque(PlaceOfWorship):
    """A mosque."""
    schema_type: ClassVar[str] = "Mosque"
