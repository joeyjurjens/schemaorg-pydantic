from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .enumeration import Enumeration


class MedicalEnumeration(Enumeration):
    """Enumerations related to health and the practice of medicine: A concept that is used to attribute a quality to another concept, as a qualifier, a collection of items or a listing of all of the elements of a set in medicine practice."""
    schema_type: ClassVar[str] = "MedicalEnumeration"
