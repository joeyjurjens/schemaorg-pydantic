from ..base import SchemaEnum


class ReservationStatusType(SchemaEnum):
    RESERVATION_CANCELLED = "https://schema.org/ReservationCancelled"
    RESERVATION_CONFIRMED = "https://schema.org/ReservationConfirmed"
    RESERVATION_HOLD = "https://schema.org/ReservationHold"
    RESERVATION_PENDING = "https://schema.org/ReservationPending"
