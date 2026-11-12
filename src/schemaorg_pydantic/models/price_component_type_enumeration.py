from ..base import SchemaEnum


class PriceComponentTypeEnumeration(SchemaEnum):
    ACTIVATION_FEE = "https://schema.org/ActivationFee"
    CLEANING_FEE = "https://schema.org/CleaningFee"
    DISTANCE_FEE = "https://schema.org/DistanceFee"
    DOWNPAYMENT = "https://schema.org/Downpayment"
    INSTALLMENT = "https://schema.org/Installment"
    SUBSCRIPTION = "https://schema.org/Subscription"
