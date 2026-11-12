from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .certification import Certification


class EnvironmentalProductDeclaration(Certification):
    """An Environmental Product Declaration (EPD) that quantifies environmental information on the life cycle of a product."""
    schema_type: ClassVar[str] = "EnvironmentalProductDeclaration"
