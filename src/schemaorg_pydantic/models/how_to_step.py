from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work import CreativeWork
from .item_list import ItemList
from .list_item import ListItem


class HowToStep(CreativeWork, ItemList, ListItem):
    """A step in the instructions for how to achieve a result. It is an ordered list with HowToDirection and/or HowToTip items."""
    schema_type: ClassVar[str] = "HowToStep"
