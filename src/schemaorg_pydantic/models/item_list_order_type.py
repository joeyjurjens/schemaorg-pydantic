from ..base import SchemaEnum


class ItemListOrderType(SchemaEnum):
    ITEM_LIST_ORDER_ASCENDING = "https://schema.org/ItemListOrderAscending"
    ITEM_LIST_ORDER_DESCENDING = "https://schema.org/ItemListOrderDescending"
    ITEM_LIST_UNORDERED = "https://schema.org/ItemListUnordered"
