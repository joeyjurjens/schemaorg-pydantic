from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class RVPark(CivicStructure):
    """A place offering space for \"Recreational Vehicles\", Caravans, mobile homes and the like."""
    schema_type: ClassVar[str] = "RVPark"
