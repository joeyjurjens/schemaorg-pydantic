from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .anatomical_structure import AnatomicalStructure


class BrainStructure(AnatomicalStructure):
    """Any anatomical structure which pertains to the soft nervous tissue functioning as the coordinating center of sensation and intellectual and nervous activity."""
    schema_type: ClassVar[str] = "BrainStructure"
