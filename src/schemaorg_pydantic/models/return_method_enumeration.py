from ..base import SchemaEnum


class ReturnMethodEnumeration(SchemaEnum):
    KEEP_PRODUCT = "https://schema.org/KeepProduct"
    RETURN_AT_KIOSK = "https://schema.org/ReturnAtKiosk"
    RETURN_BY_MAIL = "https://schema.org/ReturnByMail"
    RETURN_IN_STORE = "https://schema.org/ReturnInStore"
