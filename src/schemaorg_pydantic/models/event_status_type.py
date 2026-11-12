from ..base import SchemaEnum


class EventStatusType(SchemaEnum):
    EVENT_CANCELLED = "https://schema.org/EventCancelled"
    EVENT_MOVED_ONLINE = "https://schema.org/EventMovedOnline"
    EVENT_POSTPONED = "https://schema.org/EventPostponed"
    EVENT_RESCHEDULED = "https://schema.org/EventRescheduled"
    EVENT_SCHEDULED = "https://schema.org/EventScheduled"
