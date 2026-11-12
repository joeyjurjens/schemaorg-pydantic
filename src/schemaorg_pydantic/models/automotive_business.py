from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class AutomotiveBusiness(LocalBusiness):
    """Car repair, sales, or parts."""
    schema_type: ClassVar[str] = "AutomotiveBusiness"
