from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .thing import Thing


class Intangible(Thing):
    """A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc."""
    schema_type: ClassVar[str] = "Intangible"
