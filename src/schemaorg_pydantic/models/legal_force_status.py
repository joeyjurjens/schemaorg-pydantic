from ..base import SchemaEnum


class LegalForceStatus(SchemaEnum):
    IN_FORCE = "https://schema.org/InForce"
    NOT_IN_FORCE = "https://schema.org/NotInForce"
    PARTIALLY_IN_FORCE = "https://schema.org/PartiallyInForce"
