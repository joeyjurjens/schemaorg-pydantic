from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .creative_work import CreativeWork

if TYPE_CHECKING:
    HyperTocEntry_Ref = Union["HyperTocEntry", Ref]
else:
    HyperTocEntry_Ref = Union[Is["HyperTocEntry"], Ref]


class HyperTocEntry(CreativeWork):
    """A HyperToEntry is an item within a [[HyperToc]], which represents a hypertext table of contents for complex media objects, such as [[VideoObject]], [[AudioObject]]. The media object itself is indicated using [[associatedMedia]]. Each section of interest within that content can be described with a [[HyperTocEntry]], with associated [[startOffset]] and [[endOffset]]. When several entries are all from the same file, [[associatedMedia]] is used on the overarching [[HyperTocEntry]]; if the content has been split into multiple files, they can be referenced using [[associatedMedia]] on each [[HyperTocEntry]]."""
    schema_type: ClassVar[str] = "HyperTocEntry"
    toc_continuation: HyperTocEntry_Ref | list[HyperTocEntry_Ref] | None = Field(default=None, validation_alias="tocContinuation", serialization_alias="tocContinuation")
    utterances: Text | list[Text] | None = Field(default=None)
