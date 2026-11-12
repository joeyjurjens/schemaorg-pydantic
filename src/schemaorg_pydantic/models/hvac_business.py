from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .home_and_construction_business import HomeAndConstructionBusiness


class HVACBusiness(HomeAndConstructionBusiness):
    """A business that provides Heating, Ventilation and Air Conditioning services."""
    schema_type: ClassVar[str] = "HVACBusiness"
