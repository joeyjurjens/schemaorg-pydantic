from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .vehicle import Vehicle


class Motorcycle(Vehicle):
    """A motorcycle or motorbike is a single-track, two-wheeled motor vehicle."""
    schema_type: ClassVar[str] = "Motorcycle"
