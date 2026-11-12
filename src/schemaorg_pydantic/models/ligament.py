from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .anatomical_structure import AnatomicalStructure


class Ligament(AnatomicalStructure):
    """A short band of tough, flexible, fibrous connective tissue that functions to connect multiple bones, cartilages, and structurally support joints."""
    schema_type: ClassVar[str] = "Ligament"
