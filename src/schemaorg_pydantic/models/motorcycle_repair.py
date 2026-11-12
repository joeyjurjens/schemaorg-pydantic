from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .automotive_business import AutomotiveBusiness


class MotorcycleRepair(AutomotiveBusiness):
    """A motorcycle repair shop."""
    schema_type: ClassVar[str] = "MotorcycleRepair"
