from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .intangible import Intangible

if TYPE_CHECKING:
    from .place import Place

if TYPE_CHECKING:
    GeospatialGeometry_Place_Ref = Union["GeospatialGeometry", Place, Ref]
else:
    GeospatialGeometry_Place_Ref = Union[Is["GeospatialGeometry"], Is["Place"], Ref]


class GeospatialGeometry(Intangible):
    """(Eventually to be defined as) a supertype of GeoShape designed to accommodate definitions from Geo-Spatial best practices."""
    schema_type: ClassVar[str] = "GeospatialGeometry"
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
