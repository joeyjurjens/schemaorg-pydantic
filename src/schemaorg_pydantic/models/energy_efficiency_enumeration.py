from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .enumeration import Enumeration


class EnergyEfficiencyEnumeration(Enumeration):
    """Enumerates energy efficiency levels (also known as \"classes\" or \"ratings\") and certifications that are part of several international energy efficiency standards."""
    schema_type: ClassVar[str] = "EnergyEfficiencyEnumeration"
