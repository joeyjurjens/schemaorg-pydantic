from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .episode import Episode

if TYPE_CHECKING:
    from .language import Language

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]


class TVEpisode(Episode):
    """A TV episode which can be part of a series or season."""
    schema_type: ClassVar[str] = "TVEpisode"
    subtitle_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="subtitleLanguage", serialization_alias="subtitleLanguage")
    title_eidr: Text | list[Text] | None = Field(default=None, validation_alias="titleEIDR", serialization_alias="titleEIDR")
