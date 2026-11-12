from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class HomeAndConstructionBusiness(LocalBusiness):
    """A construction business."""
    schema_type: ClassVar[str] = "HomeAndConstructionBusiness"
