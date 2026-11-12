from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class Cemetery(CivicStructure):
    """A graveyard."""
    schema_type: ClassVar[str] = "Cemetery"
