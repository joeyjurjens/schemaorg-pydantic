from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class EmergencyService(LocalBusiness):
    """An emergency service, such as a fire station or ER."""
    schema_type: ClassVar[str] = "EmergencyService"
