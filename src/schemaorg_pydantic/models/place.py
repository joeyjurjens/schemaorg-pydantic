from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Integer, Is, Number, Ref, Text, Url
from .thing import Thing

if TYPE_CHECKING:
    from .aggregate_rating import AggregateRating
    from .certification import Certification
    from .defined_term import DefinedTerm
    from .event import Event
    from .geo_coordinates import GeoCoordinates
    from .geo_shape import GeoShape
    from .geospatial_geometry import GeospatialGeometry
    from .image_object import ImageObject
    from .location_feature_specification import LocationFeatureSpecification
    from .map import Map
    from .opening_hours_specification import OpeningHoursSpecification
    from .photograph import Photograph
    from .postal_address import PostalAddress
    from .property_value import PropertyValue
    from .review import Review

if TYPE_CHECKING:
    AggregateRating_Ref = Union[AggregateRating, Ref]
else:
    AggregateRating_Ref = Union[Is["AggregateRating"], Ref]

if TYPE_CHECKING:
    Certification_Ref = Union[Certification, Ref]
else:
    Certification_Ref = Union[Is["Certification"], Ref]

if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]

if TYPE_CHECKING:
    Event_Ref = Union[Event, Ref]
else:
    Event_Ref = Union[Is["Event"], Ref]

if TYPE_CHECKING:
    GeoCoordinates_GeoShape_Ref = Union[GeoCoordinates, GeoShape, Ref]
else:
    GeoCoordinates_GeoShape_Ref = Union[Is["GeoCoordinates"], Is["GeoShape"], Ref]

if TYPE_CHECKING:
    GeospatialGeometry_Place_Ref = Union[GeospatialGeometry, "Place", Ref]
else:
    GeospatialGeometry_Place_Ref = Union[Is["GeospatialGeometry"], Is["Place"], Ref]

if TYPE_CHECKING:
    ImageObject_Photograph_Ref = Union[ImageObject, Photograph, Ref]
else:
    ImageObject_Photograph_Ref = Union[Is["ImageObject"], Is["Photograph"], Ref]

if TYPE_CHECKING:
    ImageObject_Url_Ref = Union[ImageObject, Url, Ref]
else:
    ImageObject_Url_Ref = Union[Is["ImageObject"], Url, Ref]

if TYPE_CHECKING:
    LocationFeatureSpecification_Ref = Union[LocationFeatureSpecification, Ref]
else:
    LocationFeatureSpecification_Ref = Union[Is["LocationFeatureSpecification"], Ref]

if TYPE_CHECKING:
    Map_Url_Ref = Union[Map, Url, Ref]
else:
    Map_Url_Ref = Union[Is["Map"], Url, Ref]

Number_Text = Union[Number, Text]
if TYPE_CHECKING:
    OpeningHoursSpecification_Ref = Union[OpeningHoursSpecification, Ref]
else:
    OpeningHoursSpecification_Ref = Union[Is["OpeningHoursSpecification"], Ref]

if TYPE_CHECKING:
    Place_Ref = Union["Place", Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]

if TYPE_CHECKING:
    PostalAddress_Text_Ref = Union[PostalAddress, Text, Ref]
else:
    PostalAddress_Text_Ref = Union[Is["PostalAddress"], Text, Ref]

if TYPE_CHECKING:
    PropertyValue_Ref = Union[PropertyValue, Ref]
else:
    PropertyValue_Ref = Union[Is["PropertyValue"], Ref]

if TYPE_CHECKING:
    Review_Ref = Union[Review, Ref]
else:
    Review_Ref = Union[Is["Review"], Ref]


class Place(Thing):
    """Entities that have a somewhat fixed, physical extension."""
    schema_type: ClassVar[str] = "Place"
    additional_property: PropertyValue_Ref | list[PropertyValue_Ref] | None = Field(default=None, validation_alias="additionalProperty", serialization_alias="additionalProperty")
    address: PostalAddress_Text_Ref | list[PostalAddress_Text_Ref] | None = Field(default=None)
    aggregate_rating: AggregateRating_Ref | list[AggregateRating_Ref] | None = Field(default=None, validation_alias="aggregateRating", serialization_alias="aggregateRating")
    amenity_feature: LocationFeatureSpecification_Ref | list[LocationFeatureSpecification_Ref] | None = Field(default=None, validation_alias="amenityFeature", serialization_alias="amenityFeature")
    branch_code: Text | list[Text] | None = Field(default=None, validation_alias="branchCode", serialization_alias="branchCode")
    contained_in_place: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="containedInPlace", serialization_alias="containedInPlace")
    contains_place: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="containsPlace", serialization_alias="containsPlace")
    event: Event_Ref | list[Event_Ref] | None = Field(default=None)
    fax_number: Text | list[Text] | None = Field(default=None, validation_alias="faxNumber", serialization_alias="faxNumber")
    geo: GeoCoordinates_GeoShape_Ref | list[GeoCoordinates_GeoShape_Ref] | None = Field(default=None)
    geo_contains: GeospatialGeometry_Place_Ref | list[GeospatialGeometry_Place_Ref] | None = Field(default=None, validation_alias="geoContains", serialization_alias="geoContains")
    geo_covered_by: GeospatialGeometry_Place_Ref | list[GeospatialGeometry_Place_Ref] | None = Field(default=None, validation_alias="geoCoveredBy", serialization_alias="geoCoveredBy")
    geo_covers: GeospatialGeometry_Place_Ref | list[GeospatialGeometry_Place_Ref] | None = Field(default=None, validation_alias="geoCovers", serialization_alias="geoCovers")
    geo_crosses: GeospatialGeometry_Place_Ref | list[GeospatialGeometry_Place_Ref] | None = Field(default=None, validation_alias="geoCrosses", serialization_alias="geoCrosses")
    geo_disjoint: GeospatialGeometry_Place_Ref | list[GeospatialGeometry_Place_Ref] | None = Field(default=None, validation_alias="geoDisjoint", serialization_alias="geoDisjoint")
    geo_equals: GeospatialGeometry_Place_Ref | list[GeospatialGeometry_Place_Ref] | None = Field(default=None, validation_alias="geoEquals", serialization_alias="geoEquals")
    geo_intersects: GeospatialGeometry_Place_Ref | list[GeospatialGeometry_Place_Ref] | None = Field(default=None, validation_alias="geoIntersects", serialization_alias="geoIntersects")
    geo_overlaps: GeospatialGeometry_Place_Ref | list[GeospatialGeometry_Place_Ref] | None = Field(default=None, validation_alias="geoOverlaps", serialization_alias="geoOverlaps")
    geo_touches: GeospatialGeometry_Place_Ref | list[GeospatialGeometry_Place_Ref] | None = Field(default=None, validation_alias="geoTouches", serialization_alias="geoTouches")
    geo_within: GeospatialGeometry_Place_Ref | list[GeospatialGeometry_Place_Ref] | None = Field(default=None, validation_alias="geoWithin", serialization_alias="geoWithin")
    global_location_number: Text | list[Text] | None = Field(default=None, validation_alias="globalLocationNumber", serialization_alias="globalLocationNumber")
    has_certification: Certification_Ref | list[Certification_Ref] | None = Field(default=None, validation_alias="hasCertification", serialization_alias="hasCertification")
    has_drive_through_service: Boolean | list[Boolean] | None = Field(default=None, validation_alias="hasDriveThroughService", serialization_alias="hasDriveThroughService")
    has_gs1_digital_link: Url | list[Url] | None = Field(default=None, validation_alias="hasGS1DigitalLink", serialization_alias="hasGS1DigitalLink")
    has_map: Map_Url_Ref | list[Map_Url_Ref] | None = Field(default=None, validation_alias="hasMap", serialization_alias="hasMap")
    is_accessible_for_free: Boolean | list[Boolean] | None = Field(default=None, validation_alias="isAccessibleForFree", serialization_alias="isAccessibleForFree")
    isic_v4: Text | list[Text] | None = Field(default=None, validation_alias="isicV4", serialization_alias="isicV4")
    keywords: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    latitude: Number_Text | list[Number_Text] | None = Field(default=None)
    logo: ImageObject_Url_Ref | list[ImageObject_Url_Ref] | None = Field(default=None)
    longitude: Number_Text | list[Number_Text] | None = Field(default=None)
    maximum_attendee_capacity: Integer | list[Integer] | None = Field(default=None, validation_alias="maximumAttendeeCapacity", serialization_alias="maximumAttendeeCapacity")
    opening_hours_specification: OpeningHoursSpecification_Ref | list[OpeningHoursSpecification_Ref] | None = Field(default=None, validation_alias="openingHoursSpecification", serialization_alias="openingHoursSpecification")
    photo: ImageObject_Photograph_Ref | list[ImageObject_Photograph_Ref] | None = Field(default=None)
    public_access: Boolean | list[Boolean] | None = Field(default=None, validation_alias="publicAccess", serialization_alias="publicAccess")
    review: Review_Ref | list[Review_Ref] | None = Field(default=None)
    slogan: Text | list[Text] | None = Field(default=None)
    smoking_allowed: Boolean | list[Boolean] | None = Field(default=None, validation_alias="smokingAllowed", serialization_alias="smokingAllowed")
    special_opening_hours_specification: OpeningHoursSpecification_Ref | list[OpeningHoursSpecification_Ref] | None = Field(default=None, validation_alias="specialOpeningHoursSpecification", serialization_alias="specialOpeningHoursSpecification")
    telephone: Text | list[Text] | None = Field(default=None)
    tour_booking_page: Url | list[Url] | None = Field(default=None, validation_alias="tourBookingPage", serialization_alias="tourBookingPage")
