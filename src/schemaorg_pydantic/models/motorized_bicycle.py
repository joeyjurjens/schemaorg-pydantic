from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .vehicle import Vehicle


class MotorizedBicycle(Vehicle):
    """A motorized bicycle is a bicycle with an attached motor used to power the vehicle, or to assist with pedaling."""
    schema_type: ClassVar[str] = "MotorizedBicycle"
