from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .home_and_construction_business import HomeAndConstructionBusiness


class RoofingContractor(HomeAndConstructionBusiness):
    """A roofing contractor."""
    schema_type: ClassVar[str] = "RoofingContractor"
