from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .item_list import ItemList


class BreadcrumbList(ItemList):
    """A BreadcrumbList is an ItemList consisting of a chain of linked Web pages, typically described using at least their URL and their name, and typically ending with the current page."""
    schema_type: ClassVar[str] = "BreadcrumbList"
