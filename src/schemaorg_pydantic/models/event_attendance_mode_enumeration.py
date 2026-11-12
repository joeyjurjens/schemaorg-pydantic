from ..base import SchemaEnum


class EventAttendanceModeEnumeration(SchemaEnum):
    MIXED_EVENT_ATTENDANCE_MODE = "https://schema.org/MixedEventAttendanceMode"
    OFFLINE_EVENT_ATTENDANCE_MODE = "https://schema.org/OfflineEventAttendanceMode"
    ONLINE_EVENT_ATTENDANCE_MODE = "https://schema.org/OnlineEventAttendanceMode"
