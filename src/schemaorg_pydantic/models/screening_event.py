from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .event import Event

if TYPE_CHECKING:
    from .language import Language
    from .movie import Movie

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]

if TYPE_CHECKING:
    Movie_Ref = Union[Movie, Ref]
else:
    Movie_Ref = Union[Is["Movie"], Ref]


class ScreeningEvent(Event):
    """A screening of a movie or other video."""
    schema_type: ClassVar[str] = "ScreeningEvent"
    subtitle_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="subtitleLanguage", serialization_alias="subtitleLanguage")
    video_format: Text | list[Text] | None = Field(default=None, validation_alias="videoFormat", serialization_alias="videoFormat")
    work_presented: Movie_Ref | list[Movie_Ref] | None = Field(default=None, validation_alias="workPresented", serialization_alias="workPresented")
