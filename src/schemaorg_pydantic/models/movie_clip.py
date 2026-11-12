from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .clip import Clip


class MovieClip(Clip):
    """A short segment/part of a movie."""
    schema_type: ClassVar[str] = "MovieClip"
