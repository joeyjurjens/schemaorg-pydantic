from ..base import SchemaEnum


class IncentiveStatus(SchemaEnum):
    INCENTIVE_STATUS_ACTIVE = "https://schema.org/IncentiveStatusActive"
    INCENTIVE_STATUS_IN_DEVELOPMENT = "https://schema.org/IncentiveStatusInDevelopment"
    INCENTIVE_STATUS_ON_HOLD = "https://schema.org/IncentiveStatusOnHold"
    INCENTIVE_STATUS_RETIRED = "https://schema.org/IncentiveStatusRetired"
