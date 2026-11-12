from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .structured_value import StructuredValue


class PostalCodeRangeSpecification(StructuredValue):
    """Indicates a range of postal codes, usually defined as the set of valid codes between [[postalCodeBegin]] and [[postalCodeEnd]], inclusively."""
    schema_type: ClassVar[str] = "PostalCodeRangeSpecification"
    postal_code_begin: Text | list[Text] | None = Field(default=None, validation_alias="postalCodeBegin", serialization_alias="postalCodeBegin")
    postal_code_end: Text | list[Text] | None = Field(default=None, validation_alias="postalCodeEnd", serialization_alias="postalCodeEnd")
