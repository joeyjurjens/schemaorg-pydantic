from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .enumeration import Enumeration


class MeasurementTypeEnumeration(Enumeration):
    """Enumeration of common measurement types (or dimensions), for example \"chest\" for a person, \"inseam\" for pants, \"gauge\" for screws, or \"wheel\" for bicycles."""
    schema_type: ClassVar[str] = "MeasurementTypeEnumeration"
