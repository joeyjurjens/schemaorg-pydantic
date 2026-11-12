from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .landform import Landform


class Mountain(Landform):
    """A mountain, like Mount Whitney or Mount Everest."""
    schema_type: ClassVar[str] = "Mountain"
