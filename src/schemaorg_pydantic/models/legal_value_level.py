from ..base import SchemaEnum


class LegalValueLevel(SchemaEnum):
    AUTHORITATIVE_LEGAL_VALUE = "https://schema.org/AuthoritativeLegalValue"
    DEFINITIVE_LEGAL_VALUE = "https://schema.org/DefinitiveLegalValue"
    OFFICIAL_LEGAL_VALUE = "https://schema.org/OfficialLegalValue"
    UNOFFICIAL_LEGAL_VALUE = "https://schema.org/UnofficialLegalValue"
