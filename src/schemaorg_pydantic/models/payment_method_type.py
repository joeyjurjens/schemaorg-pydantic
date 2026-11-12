from ..base import SchemaEnum


class PaymentMethodType(SchemaEnum):
    BY_BANK_TRANSFER_IN_ADVANCE = "https://schema.org/ByBankTransferInAdvance"
    BY_INVOICE = "https://schema.org/ByInvoice"
    COD = "https://schema.org/COD"
    CASH = "https://schema.org/Cash"
    CHECK_IN_ADVANCE = "https://schema.org/CheckInAdvance"
    DIRECT_DEBIT = "https://schema.org/DirectDebit"
    IN_STORE_PREPAY = "https://schema.org/InStorePrepay"
    PHONE_CARRIER_PAYMENT = "https://schema.org/PhoneCarrierPayment"
