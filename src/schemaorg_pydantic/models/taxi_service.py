from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .service import Service


class TaxiService(Service):
    """A service for a vehicle for hire with a driver for local travel. Fares are usually calculated based on distance traveled."""
    schema_type: ClassVar[str] = "TaxiService"
