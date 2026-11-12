from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .place_of_worship import PlaceOfWorship


class Church(PlaceOfWorship):
    """A church."""
    schema_type: ClassVar[str] = "Church"
