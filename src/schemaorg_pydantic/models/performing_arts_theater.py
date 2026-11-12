from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class PerformingArtsTheater(CivicStructure):
    """A theater or other performing art center."""
    schema_type: ClassVar[str] = "PerformingArtsTheater"
