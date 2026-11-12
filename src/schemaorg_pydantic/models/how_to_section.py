from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work import CreativeWork
from .item_list import ItemList
from .list_item import ListItem


class HowToSection(CreativeWork, ItemList, ListItem):
    """A sub-grouping of steps in the instructions for how to achieve a result (e.g. steps for making a pie crust within a pie recipe)."""
    schema_type: ClassVar[str] = "HowToSection"
