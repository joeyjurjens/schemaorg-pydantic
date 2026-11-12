from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .anatomical_structure import AnatomicalStructure


class Vessel(AnatomicalStructure):
    """A component of the human body circulatory system comprised of an intricate network of hollow tubes that transport blood throughout the entire body."""
    schema_type: ClassVar[str] = "Vessel"
