from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .create_action import CreateAction

if TYPE_CHECKING:
    from .language import Language

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]


class WriteAction(CreateAction):
    """The act of authoring written creative content."""
    schema_type: ClassVar[str] = "WriteAction"
    in_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="inLanguage", serialization_alias="inLanguage")
