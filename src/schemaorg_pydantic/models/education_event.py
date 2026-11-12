from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .event import Event

if TYPE_CHECKING:
    from .defined_term import DefinedTerm

if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]


class EducationEvent(Event):
    """Event type: Education event."""
    schema_type: ClassVar[str] = "EducationEvent"
    assesses: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    educational_level: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="educationalLevel", serialization_alias="educationalLevel")
    teaches: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
