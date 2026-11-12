from ..base import SchemaEnum


class DrugPrescriptionStatus(SchemaEnum):
    OTC = "https://schema.org/OTC"
    PRESCRIPTION_ONLY = "https://schema.org/PrescriptionOnly"
