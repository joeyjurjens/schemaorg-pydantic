from ..base import SchemaEnum


class ActionStatusType(SchemaEnum):
    ACTIVE_ACTION_STATUS = "https://schema.org/ActiveActionStatus"
    COMPLETED_ACTION_STATUS = "https://schema.org/CompletedActionStatus"
    FAILED_ACTION_STATUS = "https://schema.org/FailedActionStatus"
    POTENTIAL_ACTION_STATUS = "https://schema.org/PotentialActionStatus"
