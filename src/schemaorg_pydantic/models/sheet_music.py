from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work import CreativeWork


class SheetMusic(CreativeWork):
    """Printed music, as opposed to performed or recorded music."""
    schema_type: ClassVar[str] = "SheetMusic"
