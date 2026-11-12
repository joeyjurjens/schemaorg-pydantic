from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .item_list import ItemList


class OfferCatalog(ItemList):
    """An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs that are offeredBy the same provider."""
    schema_type: ClassVar[str] = "OfferCatalog"
