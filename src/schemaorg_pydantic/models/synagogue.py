from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .place_of_worship import PlaceOfWorship


class Synagogue(PlaceOfWorship):
    """A synagogue."""
    schema_type: ClassVar[str] = "Synagogue"
