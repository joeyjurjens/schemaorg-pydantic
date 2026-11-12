from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class MusicStore(Store):
    """A music store."""
    schema_type: ClassVar[str] = "MusicStore"
