from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class EmploymentAgency(LocalBusiness):
    """An employment agency."""
    schema_type: ClassVar[str] = "EmploymentAgency"
