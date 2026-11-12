from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class BoatTerminal(CivicStructure):
    """A terminal for boats, ships, and other water vessels."""
    schema_type: ClassVar[str] = "BoatTerminal"
