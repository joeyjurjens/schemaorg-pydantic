from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .automotive_business import AutomotiveBusiness


class AutoRental(AutomotiveBusiness):
    """A car rental business."""
    schema_type: ClassVar[str] = "AutoRental"
