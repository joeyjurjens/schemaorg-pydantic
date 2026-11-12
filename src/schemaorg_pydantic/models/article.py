from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref, Text, Url
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .speakable_specification import SpeakableSpecification

if TYPE_CHECKING:
    CreativeWork_Text_Ref = Union[CreativeWork, Text, Ref]
else:
    CreativeWork_Text_Ref = Union[Is["CreativeWork"], Text, Ref]

Integer_Text = Union[Integer, Text]
if TYPE_CHECKING:
    SpeakableSpecification_Url_Ref = Union[SpeakableSpecification, Url, Ref]
else:
    SpeakableSpecification_Url_Ref = Union[Is["SpeakableSpecification"], Url, Ref]


class Article(CreativeWork):
    """An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all."""
    schema_type: ClassVar[str] = "Article"
    article_body: Text | list[Text] | None = Field(default=None, validation_alias="articleBody", serialization_alias="articleBody")
    article_section: Text | list[Text] | None = Field(default=None, validation_alias="articleSection", serialization_alias="articleSection")
    backstory: CreativeWork_Text_Ref | list[CreativeWork_Text_Ref] | None = Field(default=None)
    page_end: Integer_Text | list[Integer_Text] | None = Field(default=None, validation_alias="pageEnd", serialization_alias="pageEnd")
    page_start: Integer_Text | list[Integer_Text] | None = Field(default=None, validation_alias="pageStart", serialization_alias="pageStart")
    pagination: Text | list[Text] | None = Field(default=None)
    speakable: SpeakableSpecification_Url_Ref | list[SpeakableSpecification_Url_Ref] | None = Field(default=None)
