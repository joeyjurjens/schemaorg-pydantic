from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Integer, Is, Number, Ref, Text
from .place import Place

if TYPE_CHECKING:
    from .bed_details import BedDetails
    from .bed_type import BedType
    from .floor_plan import FloorPlan
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    BedDetails_BedType_Text_Ref = Union[BedDetails, BedType, Text, Ref]
else:
    BedDetails_BedType_Text_Ref = Union[Is["BedDetails"], Is["BedType"], Text, Ref]

Boolean_Text = Union[Boolean, Text]
if TYPE_CHECKING:
    FloorPlan_Ref = Union[FloorPlan, Ref]
else:
    FloorPlan_Ref = Union[Is["FloorPlan"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Number_Ref = Union[QuantitativeValue, Number, Ref]
else:
    QuantitativeValue_Number_Ref = Union[Is["QuantitativeValue"], Number, Ref]

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class Accommodation(Place):
    """An accommodation is a place that can accommodate human beings, e.g. a hotel room, a camping pitch, or a meeting room. Many accommodations are for overnight stays, but this is not a mandatory requirement.\nFor more specific types of accommodations not defined in schema.org, one can use [[additionalType]] with external vocabularies.\n<br /><br />\nSee also the <a href=\"/docs/hotels.html\">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>."""
    schema_type: ClassVar[str] = "Accommodation"
    accommodation_category: Text | list[Text] | None = Field(default=None, validation_alias="accommodationCategory", serialization_alias="accommodationCategory")
    accommodation_floor_plan: FloorPlan_Ref | list[FloorPlan_Ref] | None = Field(default=None, validation_alias="accommodationFloorPlan", serialization_alias="accommodationFloorPlan")
    bed: BedDetails_BedType_Text_Ref | list[BedDetails_BedType_Text_Ref] | None = Field(default=None)
    floor_level: Text | list[Text] | None = Field(default=None, validation_alias="floorLevel", serialization_alias="floorLevel")
    floor_size: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="floorSize", serialization_alias="floorSize")
    lease_length: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None, validation_alias="leaseLength", serialization_alias="leaseLength")
    number_of_bathrooms_total: Integer | list[Integer] | None = Field(default=None, validation_alias="numberOfBathroomsTotal", serialization_alias="numberOfBathroomsTotal")
    number_of_bedrooms: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="numberOfBedrooms", serialization_alias="numberOfBedrooms")
    number_of_full_bathrooms: Number | list[Number] | None = Field(default=None, validation_alias="numberOfFullBathrooms", serialization_alias="numberOfFullBathrooms")
    number_of_partial_bathrooms: Number | list[Number] | None = Field(default=None, validation_alias="numberOfPartialBathrooms", serialization_alias="numberOfPartialBathrooms")
    number_of_rooms: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="numberOfRooms", serialization_alias="numberOfRooms")
    occupancy: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None)
    permitted_usage: Text | list[Text] | None = Field(default=None, validation_alias="permittedUsage", serialization_alias="permittedUsage")
    pets_allowed: Boolean_Text | list[Boolean_Text] | None = Field(default=None, validation_alias="petsAllowed", serialization_alias="petsAllowed")
    year_built: Number | list[Number] | None = Field(default=None, validation_alias="yearBuilt", serialization_alias="yearBuilt")
