from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .intangible import Intangible


class StructuredValue(Intangible):
    """Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing."""
    schema_type: ClassVar[str] = "StructuredValue"
