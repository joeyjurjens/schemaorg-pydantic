from ..base import SchemaEnum


class ReturnFeesEnumeration(SchemaEnum):
    FREE_RETURN = "https://schema.org/FreeReturn"
    ORIGINAL_SHIPPING_FEES = "https://schema.org/OriginalShippingFees"
    RESTOCKING_FEES = "https://schema.org/RestockingFees"
    RETURN_FEES_CUSTOMER_RESPONSIBILITY = "https://schema.org/ReturnFeesCustomerResponsibility"
    RETURN_SHIPPING_FEES = "https://schema.org/ReturnShippingFees"
