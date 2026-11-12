from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class ParkingFacility(CivicStructure):
    """A parking lot or other parking facility."""
    schema_type: ClassVar[str] = "ParkingFacility"
