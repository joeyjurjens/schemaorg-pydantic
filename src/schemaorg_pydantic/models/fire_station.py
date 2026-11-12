from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure
from .emergency_service import EmergencyService


class FireStation(CivicStructure, EmergencyService):
    """A fire station. With firemen."""
    schema_type: ClassVar[str] = "FireStation"
