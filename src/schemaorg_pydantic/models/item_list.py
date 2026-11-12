from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref, Text
from .intangible import Intangible
from .item_list_order_type import ItemListOrderType

if TYPE_CHECKING:
    from .list_item import ListItem
    from .thing import Thing

ItemListOrderType_Text = Union[ItemListOrderType, Text]
if TYPE_CHECKING:
    ListItem_Thing_Text_Ref = Union[ListItem, Thing, Text, Ref]
else:
    ListItem_Thing_Text_Ref = Union[Is["ListItem"], Is["Thing"], Text, Ref]

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]


class ItemList(Intangible):
    """A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting."""
    schema_type: ClassVar[str] = "ItemList"
    aggregate_element: Thing_Ref | list[Thing_Ref] | None = Field(default=None, validation_alias="aggregateElement", serialization_alias="aggregateElement")
    item_list_element: ListItem_Thing_Text_Ref | list[ListItem_Thing_Text_Ref] | None = Field(default=None, validation_alias="itemListElement", serialization_alias="itemListElement")
    item_list_order: ItemListOrderType_Text | list[ItemListOrderType_Text] | None = Field(default=None, validation_alias="itemListOrder", serialization_alias="itemListOrder")
    number_of_items: Integer | list[Integer] | None = Field(default=None, validation_alias="numberOfItems", serialization_alias="numberOfItems")
