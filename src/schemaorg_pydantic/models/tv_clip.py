from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .clip import Clip


class TVClip(Clip):
    """A short TV program or a segment/part of a TV program."""
    schema_type: ClassVar[str] = "TVClip"
