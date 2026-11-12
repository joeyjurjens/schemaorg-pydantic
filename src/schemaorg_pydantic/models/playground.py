from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class Playground(CivicStructure):
    """A playground."""
    schema_type: ClassVar[str] = "Playground"
