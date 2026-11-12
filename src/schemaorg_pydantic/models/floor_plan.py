from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Integer, Is, Number, Ref, Text, Url
from .intangible import Intangible

if TYPE_CHECKING:
    from .accommodation import Accommodation
    from .image_object import ImageObject
    from .location_feature_specification import LocationFeatureSpecification
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    Accommodation_Ref = Union[Accommodation, Ref]
else:
    Accommodation_Ref = Union[Is["Accommodation"], Ref]

Boolean_Text = Union[Boolean, Text]
if TYPE_CHECKING:
    ImageObject_Url_Ref = Union[ImageObject, Url, Ref]
else:
    ImageObject_Url_Ref = Union[Is["ImageObject"], Url, Ref]

if TYPE_CHECKING:
    LocationFeatureSpecification_Ref = Union[LocationFeatureSpecification, Ref]
else:
    LocationFeatureSpecification_Ref = Union[Is["LocationFeatureSpecification"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Number_Ref = Union[QuantitativeValue, Number, Ref]
else:
    QuantitativeValue_Number_Ref = Union[Is["QuantitativeValue"], Number, Ref]

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]


class FloorPlan(Intangible):
    """A FloorPlan is an explicit representation of a collection of similar accommodations, allowing the provision of common information (room counts, sizes, layout diagrams) and offers for rental or sale. In typical use, some [[ApartmentComplex]] has an [[accommodationFloorPlan]] which is a [[FloorPlan]].  A FloorPlan is always in the context of a particular place, either a larger [[ApartmentComplex]] or a single [[Apartment]]. The visual/spatial aspects of a floor plan (i.e. room layout, [see wikipedia](https://en.wikipedia.org/wiki/Floor_plan)) can be indicated using [[image]]."""
    schema_type: ClassVar[str] = "FloorPlan"
    amenity_feature: LocationFeatureSpecification_Ref | list[LocationFeatureSpecification_Ref] | None = Field(default=None, validation_alias="amenityFeature", serialization_alias="amenityFeature")
    floor_size: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="floorSize", serialization_alias="floorSize")
    is_plan_for_apartment: Accommodation_Ref | list[Accommodation_Ref] | None = Field(default=None, validation_alias="isPlanForApartment", serialization_alias="isPlanForApartment")
    layout_image: ImageObject_Url_Ref | list[ImageObject_Url_Ref] | None = Field(default=None, validation_alias="layoutImage", serialization_alias="layoutImage")
    number_of_accommodation_units: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="numberOfAccommodationUnits", serialization_alias="numberOfAccommodationUnits")
    number_of_available_accommodation_units: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="numberOfAvailableAccommodationUnits", serialization_alias="numberOfAvailableAccommodationUnits")
    number_of_bathrooms_total: Integer | list[Integer] | None = Field(default=None, validation_alias="numberOfBathroomsTotal", serialization_alias="numberOfBathroomsTotal")
    number_of_bedrooms: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="numberOfBedrooms", serialization_alias="numberOfBedrooms")
    number_of_full_bathrooms: Number | list[Number] | None = Field(default=None, validation_alias="numberOfFullBathrooms", serialization_alias="numberOfFullBathrooms")
    number_of_partial_bathrooms: Number | list[Number] | None = Field(default=None, validation_alias="numberOfPartialBathrooms", serialization_alias="numberOfPartialBathrooms")
    number_of_rooms: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="numberOfRooms", serialization_alias="numberOfRooms")
    pets_allowed: Boolean_Text | list[Boolean_Text] | None = Field(default=None, validation_alias="petsAllowed", serialization_alias="petsAllowed")
