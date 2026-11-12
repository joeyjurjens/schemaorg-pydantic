from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class TrainStation(CivicStructure):
    """A train station."""
    schema_type: ClassVar[str] = "TrainStation"
