from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .product import Product


class IndividualProduct(Product):
    """A single, identifiable product instance (e.g. a laptop with a particular serial number)."""
    schema_type: ClassVar[str] = "IndividualProduct"
    serial_number: Text | list[Text] | None = Field(default=None, validation_alias="serialNumber", serialization_alias="serialNumber")
