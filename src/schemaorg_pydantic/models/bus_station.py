from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class BusStation(CivicStructure):
    """A bus station."""
    schema_type: ClassVar[str] = "BusStation"
