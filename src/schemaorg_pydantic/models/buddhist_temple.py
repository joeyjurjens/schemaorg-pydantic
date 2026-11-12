from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .place_of_worship import PlaceOfWorship


class BuddhistTemple(PlaceOfWorship):
    """A Buddhist temple."""
    schema_type: ClassVar[str] = "BuddhistTemple"
