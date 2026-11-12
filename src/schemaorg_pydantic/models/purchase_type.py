from ..base import SchemaEnum


class PurchaseType(SchemaEnum):
    PURCHASE_TYPE_LEASE = "https://schema.org/PurchaseTypeLease"
    PURCHASE_TYPE_NEW_PURCHASE = "https://schema.org/PurchaseTypeNewPurchase"
    PURCHASE_TYPE_TRADE_IN = "https://schema.org/PurchaseTypeTradeIn"
    PURCHASE_TYPE_USED_PURCHASE = "https://schema.org/PurchaseTypeUsedPurchase"
