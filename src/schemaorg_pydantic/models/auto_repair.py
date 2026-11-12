from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .automotive_business import AutomotiveBusiness


class AutoRepair(AutomotiveBusiness):
    """Car repair business."""
    schema_type: ClassVar[str] = "AutoRepair"
