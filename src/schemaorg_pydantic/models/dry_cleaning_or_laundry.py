from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class DryCleaningOrLaundry(LocalBusiness):
    """A dry-cleaning business."""
    schema_type: ClassVar[str] = "DryCleaningOrLaundry"
