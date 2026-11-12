from ..base import SchemaEnum


class ItemAvailability(SchemaEnum):
    BACK_ORDER = "https://schema.org/BackOrder"
    DISCONTINUED = "https://schema.org/Discontinued"
    IN_STOCK = "https://schema.org/InStock"
    IN_STORE_ONLY = "https://schema.org/InStoreOnly"
    LIMITED_AVAILABILITY = "https://schema.org/LimitedAvailability"
    MADE_TO_ORDER = "https://schema.org/MadeToOrder"
    ONLINE_ONLY = "https://schema.org/OnlineOnly"
    OUT_OF_STOCK = "https://schema.org/OutOfStock"
    PRE_ORDER = "https://schema.org/PreOrder"
    PRE_SALE = "https://schema.org/PreSale"
    RESERVED = "https://schema.org/Reserved"
    SOLD_OUT = "https://schema.org/SoldOut"
