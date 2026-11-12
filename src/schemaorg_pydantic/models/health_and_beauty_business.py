from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class HealthAndBeautyBusiness(LocalBusiness):
    """Health and beauty."""
    schema_type: ClassVar[str] = "HealthAndBeautyBusiness"
