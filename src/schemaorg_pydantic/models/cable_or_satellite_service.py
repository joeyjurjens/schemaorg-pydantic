from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .service import Service


class CableOrSatelliteService(Service):
    """A service which provides access to media programming like TV or radio. Access may be via cable or satellite."""
    schema_type: ClassVar[str] = "CableOrSatelliteService"
