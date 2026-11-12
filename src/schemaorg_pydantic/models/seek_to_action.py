from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref
from .action import Action

if TYPE_CHECKING:
    from .hyper_toc_entry import HyperTocEntry

if TYPE_CHECKING:
    HyperTocEntry_Number_Ref = Union[HyperTocEntry, Number, Ref]
else:
    HyperTocEntry_Number_Ref = Union[Is["HyperTocEntry"], Number, Ref]


class SeekToAction(Action):
    """This is the [[Action]] of navigating to a specific [[startOffset]] timestamp within a [[VideoObject]], typically represented with a URL template structure."""
    schema_type: ClassVar[str] = "SeekToAction"
    start_offset: HyperTocEntry_Number_Ref | list[HyperTocEntry_Number_Ref] | None = Field(default=None, validation_alias="startOffset", serialization_alias="startOffset")
