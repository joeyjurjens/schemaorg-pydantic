from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class ChildCare(LocalBusiness):
    """A Childcare center."""
    schema_type: ClassVar[str] = "ChildCare"
