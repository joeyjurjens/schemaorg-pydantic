from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure
from .emergency_service import EmergencyService


class PoliceStation(CivicStructure, EmergencyService):
    """A police station."""
    schema_type: ClassVar[str] = "PoliceStation"
