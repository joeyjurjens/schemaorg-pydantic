from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .people_audience import PeopleAudience


class MedicalAudience(PeopleAudience):
    """Target audiences for medical web pages."""
    schema_type: ClassVar[str] = "MedicalAudience"
