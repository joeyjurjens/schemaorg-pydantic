from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .health_and_beauty_business import HealthAndBeautyBusiness


class DaySpa(HealthAndBeautyBusiness):
    """A day spa."""
    schema_type: ClassVar[str] = "DaySpa"
