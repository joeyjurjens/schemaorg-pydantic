from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class BusStop(CivicStructure):
    """A bus stop."""
    schema_type: ClassVar[str] = "BusStop"
