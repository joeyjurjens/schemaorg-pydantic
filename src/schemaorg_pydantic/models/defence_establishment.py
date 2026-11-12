from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .government_building import GovernmentBuilding


class DefenceEstablishment(GovernmentBuilding):
    """A defence establishment, such as an army or navy base."""
    schema_type: ClassVar[str] = "DefenceEstablishment"
