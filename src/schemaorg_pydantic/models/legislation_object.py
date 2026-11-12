from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .legislation import Legislation
from .media_object import MediaObject
from .legal_value_level import LegalValueLevel


class LegislationObject(Legislation, MediaObject):
    """A specific object or file containing a Legislation. Note that the same Legislation can be published in multiple files. For example, a digitally signed PDF, a plain PDF and an HTML version."""
    schema_type: ClassVar[str] = "LegislationObject"
    legislation_legal_value: LegalValueLevel | list[LegalValueLevel] | None = Field(default=None, validation_alias="legislationLegalValue", serialization_alias="legislationLegalValue")
