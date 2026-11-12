from ..base import SchemaEnum


class MapCategoryType(SchemaEnum):
    PARKING_MAP = "https://schema.org/ParkingMap"
    SEATING_MAP = "https://schema.org/SeatingMap"
    TRANSIT_MAP = "https://schema.org/TransitMap"
    VENUE_MAP = "https://schema.org/VenueMap"
