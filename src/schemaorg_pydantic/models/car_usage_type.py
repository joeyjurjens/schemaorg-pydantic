from ..base import SchemaEnum


class CarUsageType(SchemaEnum):
    DRIVING_SCHOOL_VEHICLE_USAGE = "https://schema.org/DrivingSchoolVehicleUsage"
    RENTAL_VEHICLE_USAGE = "https://schema.org/RentalVehicleUsage"
    TAXI_VEHICLE_USAGE = "https://schema.org/TaxiVehicleUsage"
