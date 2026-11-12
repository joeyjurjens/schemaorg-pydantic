from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .administrative_area import AdministrativeArea


class SchoolDistrict(AdministrativeArea):
    """A School District is an administrative area for the administration of schools."""
    schema_type: ClassVar[str] = "SchoolDistrict"
