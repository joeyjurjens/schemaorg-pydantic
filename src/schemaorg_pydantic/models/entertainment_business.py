from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class EntertainmentBusiness(LocalBusiness):
    """A business providing entertainment."""
    schema_type: ClassVar[str] = "EntertainmentBusiness"
