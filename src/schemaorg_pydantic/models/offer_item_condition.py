from ..base import SchemaEnum


class OfferItemCondition(SchemaEnum):
    DAMAGED_CONDITION = "https://schema.org/DamagedCondition"
    NEW_CONDITION = "https://schema.org/NewCondition"
    REFURBISHED_CONDITION = "https://schema.org/RefurbishedCondition"
    USED_CONDITION = "https://schema.org/UsedCondition"
