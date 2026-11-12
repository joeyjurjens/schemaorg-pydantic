from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .enumeration import Enumeration


class BusinessEntityType(Enumeration):
    """A business entity type is a conceptual entity representing the legal form, the size, the main line of business, the position in the value chain, or any combination thereof, of an organization or business person."""
    schema_type: ClassVar[str] = "BusinessEntityType"
