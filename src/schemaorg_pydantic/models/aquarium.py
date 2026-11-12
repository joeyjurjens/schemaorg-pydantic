from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class Aquarium(CivicStructure):
    """Aquarium."""
    schema_type: ClassVar[str] = "Aquarium"
