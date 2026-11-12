from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class Museum(CivicStructure):
    """A museum."""
    schema_type: ClassVar[str] = "Museum"
