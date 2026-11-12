from ..base import SchemaEnum


class RefundTypeEnumeration(SchemaEnum):
    EXCHANGE_REFUND = "https://schema.org/ExchangeRefund"
    FULL_REFUND = "https://schema.org/FullRefund"
    STORE_CREDIT_REFUND = "https://schema.org/StoreCreditRefund"
