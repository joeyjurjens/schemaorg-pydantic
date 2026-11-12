from ..base import SchemaEnum


class DrugCostCategory(SchemaEnum):
    REIMBURSEMENT_CAP = "https://schema.org/ReimbursementCap"
    RETAIL = "https://schema.org/Retail"
    WHOLESALE = "https://schema.org/Wholesale"
