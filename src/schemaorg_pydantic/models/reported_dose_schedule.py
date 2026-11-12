from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .dose_schedule import DoseSchedule


class ReportedDoseSchedule(DoseSchedule):
    """A patient-reported or observed dosing schedule for a drug or supplement."""
    schema_type: ClassVar[str] = "ReportedDoseSchedule"
