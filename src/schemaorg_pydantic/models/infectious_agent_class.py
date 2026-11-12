from ..base import SchemaEnum


class InfectiousAgentClass(SchemaEnum):
    BACTERIA = "https://schema.org/Bacteria"
    FUNGUS = "https://schema.org/Fungus"
    MULTICELLULAR_PARASITE = "https://schema.org/MulticellularParasite"
    PRION = "https://schema.org/Prion"
    PROTOZOA = "https://schema.org/Protozoa"
    VIRUS = "https://schema.org/Virus"
