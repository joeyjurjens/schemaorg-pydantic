from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .creative_work import CreativeWork


class Thesis(CreativeWork):
    """A thesis or dissertation document submitted in support of candidature for an academic degree or professional qualification."""
    schema_type: ClassVar[str] = "Thesis"
    in_support_of: Text | list[Text] | None = Field(default=None, validation_alias="inSupportOf", serialization_alias="inSupportOf")
