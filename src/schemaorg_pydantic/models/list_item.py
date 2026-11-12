from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref, Text, Url
from .intangible import Intangible

if TYPE_CHECKING:
    from .thing import Thing

Integer_Text = Union[Integer, Text]
if TYPE_CHECKING:
    ListItem_Ref = Union["ListItem", Ref]
else:
    ListItem_Ref = Union[Is["ListItem"], Ref]

if TYPE_CHECKING:
    Thing_Url_Ref = Union[Thing, Url, Ref]
else:
    Thing_Url_Ref = Union[Is["Thing"], Url, Ref]


class ListItem(Intangible):
    """An list item, e.g. a step in a checklist or how-to description."""
    schema_type: ClassVar[str] = "ListItem"
    item: Thing_Url_Ref | list[Thing_Url_Ref] | None = Field(default=None)
    next_item: ListItem_Ref | list[ListItem_Ref] | None = Field(default=None, validation_alias="nextItem", serialization_alias="nextItem")
    position: Integer_Text | list[Integer_Text] | None = Field(default=None)
    previous_item: ListItem_Ref | list[ListItem_Ref] | None = Field(default=None, validation_alias="previousItem", serialization_alias="previousItem")
