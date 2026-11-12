from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .audience import Audience


class Researcher(Audience):
    """Researchers."""
    schema_type: ClassVar[str] = "Researcher"
