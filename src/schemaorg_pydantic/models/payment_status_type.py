from ..base import SchemaEnum


class PaymentStatusType(SchemaEnum):
    PAYMENT_AUTOMATICALLY_APPLIED = "https://schema.org/PaymentAutomaticallyApplied"
    PAYMENT_COMPLETE = "https://schema.org/PaymentComplete"
    PAYMENT_DECLINED = "https://schema.org/PaymentDeclined"
    PAYMENT_DUE = "https://schema.org/PaymentDue"
    PAYMENT_PAST_DUE = "https://schema.org/PaymentPastDue"
