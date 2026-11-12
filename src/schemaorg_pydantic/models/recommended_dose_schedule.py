from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .dose_schedule import DoseSchedule


class RecommendedDoseSchedule(DoseSchedule):
    """A recommended dosing schedule for a drug or supplement as prescribed or recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity."""
    schema_type: ClassVar[str] = "RecommendedDoseSchedule"
