from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class SubwayStation(CivicStructure):
    """A subway station."""
    schema_type: ClassVar[str] = "SubwayStation"
