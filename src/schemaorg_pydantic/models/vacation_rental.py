from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .lodging_business import LodgingBusiness


class VacationRental(LodgingBusiness):
    """A kind of lodging business that focuses on renting single properties for limited time."""
    schema_type: ClassVar[str] = "VacationRental"
