from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .clip import Clip


class RadioClip(Clip):
    """A short radio program or a segment/part of a radio program."""
    schema_type: ClassVar[str] = "RadioClip"
