from ..base import SchemaEnum


class MedicalStudyStatus(SchemaEnum):
    ACTIVE_NOT_RECRUITING = "https://schema.org/ActiveNotRecruiting"
    COMPLETED = "https://schema.org/Completed"
    ENROLLING_BY_INVITATION = "https://schema.org/EnrollingByInvitation"
    NOT_YET_RECRUITING = "https://schema.org/NotYetRecruiting"
    RECRUITING = "https://schema.org/Recruiting"
    RESULTS_AVAILABLE = "https://schema.org/ResultsAvailable"
    RESULTS_NOT_AVAILABLE = "https://schema.org/ResultsNotAvailable"
    SUSPENDED = "https://schema.org/Suspended"
    TERMINATED = "https://schema.org/Terminated"
    WITHDRAWN = "https://schema.org/Withdrawn"
