from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .anatomical_structure import AnatomicalStructure


class Bone(AnatomicalStructure):
    """Rigid connective tissue that comprises up the skeletal structure of the human body."""
    schema_type: ClassVar[str] = "Bone"
