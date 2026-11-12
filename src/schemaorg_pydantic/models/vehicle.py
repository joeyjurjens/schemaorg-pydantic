from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, Is, Number, Ref, Text
from .product import Product
from .car_usage_type import CarUsageType
from .drive_wheel_configuration_value import DriveWheelConfigurationValue
from .steering_position_value import SteeringPositionValue

if TYPE_CHECKING:
    from .engine_specification import EngineSpecification
    from .quantitative_value import QuantitativeValue

CarUsageType_Text = Union[CarUsageType, Text]
DriveWheelConfigurationValue_SteeringPositionValue_Text = Union[DriveWheelConfigurationValue, SteeringPositionValue, Text]
DriveWheelConfigurationValue_Text = Union[DriveWheelConfigurationValue, Text]
if TYPE_CHECKING:
    EngineSpecification_Ref = Union[EngineSpecification, Ref]
else:
    EngineSpecification_Ref = Union[Is["EngineSpecification"], Ref]

Number_Text = Union[Number, Text]
if TYPE_CHECKING:
    QuantitativeValue_Number_Ref = Union[QuantitativeValue, Number, Ref]
else:
    QuantitativeValue_Number_Ref = Union[Is["QuantitativeValue"], Number, Ref]

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]


class Vehicle(Product):
    """A vehicle is a device that is designed or used to transport people or cargo over land, water, air, or through space."""
    schema_type: ClassVar[str] = "Vehicle"
    acceleration_time: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="accelerationTime", serialization_alias="accelerationTime")
    body_type: DriveWheelConfigurationValue_SteeringPositionValue_Text | list[DriveWheelConfigurationValue_SteeringPositionValue_Text] | None = Field(default=None, validation_alias="bodyType", serialization_alias="bodyType")
    call_sign: Text | list[Text] | None = Field(default=None, validation_alias="callSign", serialization_alias="callSign")
    cargo_volume: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="cargoVolume", serialization_alias="cargoVolume")
    date_vehicle_first_registered: Date | list[Date] | None = Field(default=None, validation_alias="dateVehicleFirstRegistered", serialization_alias="dateVehicleFirstRegistered")
    drive_wheel_configuration: DriveWheelConfigurationValue_Text | list[DriveWheelConfigurationValue_Text] | None = Field(default=None, validation_alias="driveWheelConfiguration", serialization_alias="driveWheelConfiguration")
    emissions_co2: Number | list[Number] | None = Field(default=None, validation_alias="emissionsCO2", serialization_alias="emissionsCO2")
    fuel_capacity: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="fuelCapacity", serialization_alias="fuelCapacity")
    fuel_consumption: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="fuelConsumption", serialization_alias="fuelConsumption")
    fuel_efficiency: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="fuelEfficiency", serialization_alias="fuelEfficiency")
    fuel_type: DriveWheelConfigurationValue_SteeringPositionValue_Text | list[DriveWheelConfigurationValue_SteeringPositionValue_Text] | None = Field(default=None, validation_alias="fuelType", serialization_alias="fuelType")
    known_vehicle_damages: Text | list[Text] | None = Field(default=None, validation_alias="knownVehicleDamages", serialization_alias="knownVehicleDamages")
    meets_emission_standard: DriveWheelConfigurationValue_SteeringPositionValue_Text | list[DriveWheelConfigurationValue_SteeringPositionValue_Text] | None = Field(default=None, validation_alias="meetsEmissionStandard", serialization_alias="meetsEmissionStandard")
    mileage_from_odometer: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="mileageFromOdometer", serialization_alias="mileageFromOdometer")
    model_date_: Date | list[Date] | None = Field(default=None, validation_alias="modelDate", serialization_alias="modelDate")
    number_of_airbags: Number_Text | list[Number_Text] | None = Field(default=None, validation_alias="numberOfAirbags", serialization_alias="numberOfAirbags")
    number_of_axles: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="numberOfAxles", serialization_alias="numberOfAxles")
    number_of_doors: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="numberOfDoors", serialization_alias="numberOfDoors")
    number_of_forward_gears: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="numberOfForwardGears", serialization_alias="numberOfForwardGears")
    number_of_previous_owners: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="numberOfPreviousOwners", serialization_alias="numberOfPreviousOwners")
    payload: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None)
    seating_capacity: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="seatingCapacity", serialization_alias="seatingCapacity")
    speed: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None)
    steering_position: SteeringPositionValue | list[SteeringPositionValue] | None = Field(default=None, validation_alias="steeringPosition", serialization_alias="steeringPosition")
    tongue_weight: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="tongueWeight", serialization_alias="tongueWeight")
    trailer_weight: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="trailerWeight", serialization_alias="trailerWeight")
    vehicle_configuration: Text | list[Text] | None = Field(default=None, validation_alias="vehicleConfiguration", serialization_alias="vehicleConfiguration")
    vehicle_engine: EngineSpecification_Ref | list[EngineSpecification_Ref] | None = Field(default=None, validation_alias="vehicleEngine", serialization_alias="vehicleEngine")
    vehicle_identification_number: Text | list[Text] | None = Field(default=None, validation_alias="vehicleIdentificationNumber", serialization_alias="vehicleIdentificationNumber")
    vehicle_interior_color: Text | list[Text] | None = Field(default=None, validation_alias="vehicleInteriorColor", serialization_alias="vehicleInteriorColor")
    vehicle_interior_type: Text | list[Text] | None = Field(default=None, validation_alias="vehicleInteriorType", serialization_alias="vehicleInteriorType")
    vehicle_model_date: Date | list[Date] | None = Field(default=None, validation_alias="vehicleModelDate", serialization_alias="vehicleModelDate")
    vehicle_seating_capacity: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="vehicleSeatingCapacity", serialization_alias="vehicleSeatingCapacity")
    vehicle_special_usage: CarUsageType_Text | list[CarUsageType_Text] | None = Field(default=None, validation_alias="vehicleSpecialUsage", serialization_alias="vehicleSpecialUsage")
    vehicle_transmission: DriveWheelConfigurationValue_SteeringPositionValue_Text | list[DriveWheelConfigurationValue_SteeringPositionValue_Text] | None = Field(default=None, validation_alias="vehicleTransmission", serialization_alias="vehicleTransmission")
    weight_total: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="weightTotal", serialization_alias="weightTotal")
    wheelbase: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None)
