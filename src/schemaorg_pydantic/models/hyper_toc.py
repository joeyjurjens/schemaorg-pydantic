from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .hyper_toc_entry import HyperTocEntry

if TYPE_CHECKING:
    HyperTocEntry_Ref = Union[HyperTocEntry, Ref]
else:
    HyperTocEntry_Ref = Union[Is["HyperTocEntry"], Ref]


class HyperToc(CreativeWork):
    """A HyperToc represents a hypertext table of contents for complex media objects, such as [[VideoObject]], [[AudioObject]]. Items in the table of contents are indicated using the [[tocEntry]] property, and typed [[HyperTocEntry]]. For cases where the same larger work is split into multiple files, [[associatedMedia]] can be used on individual [[HyperTocEntry]] items."""
    schema_type: ClassVar[str] = "HyperToc"
    toc_entry: HyperTocEntry_Ref | list[HyperTocEntry_Ref] | None = Field(default=None, validation_alias="tocEntry", serialization_alias="tocEntry")
