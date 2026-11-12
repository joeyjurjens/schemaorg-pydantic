from ..base import SchemaEnum


class PriceTypeEnumeration(SchemaEnum):
    INVOICE_PRICE = "https://schema.org/InvoicePrice"
    LIST_PRICE = "https://schema.org/ListPrice"
    MSRP = "https://schema.org/MSRP"
    MAXIMUM_RETAIL_PRICE = "https://schema.org/MaximumRetailPrice"
    MINIMUM_ADVERTISED_PRICE = "https://schema.org/MinimumAdvertisedPrice"
    REGULAR_PRICE = "https://schema.org/RegularPrice"
    SRP = "https://schema.org/SRP"
    SALE_PRICE = "https://schema.org/SalePrice"
    STRIKETHROUGH_PRICE = "https://schema.org/StrikethroughPrice"
