from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .enumeration import Enumeration


class WarrantyScope(Enumeration):
    """A range of services that will be provided to a customer free of charge in case of a defect or malfunction of a product."""
    schema_type: ClassVar[str] = "WarrantyScope"
