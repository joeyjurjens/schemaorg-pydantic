from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .geo_shape import GeoShape

if TYPE_CHECKING:
    from .geo_coordinates import GeoCoordinates

if TYPE_CHECKING:
    GeoCoordinates_Ref = Union[GeoCoordinates, Ref]
else:
    GeoCoordinates_Ref = Union[Is["GeoCoordinates"], Ref]

Number_Text = Union[Number, Text]

class GeoCircle(GeoShape):
    """A GeoCircle is a GeoShape representing a circular geographic area. As it is a GeoShape\n          it provides the simple textual property 'circle', but also allows the combination of postalCode alongside geoRadius.\n          The center of the circle can be indicated via the 'geoMidpoint' property, or more approximately using 'address', 'postalCode'."""
    schema_type: ClassVar[str] = "GeoCircle"
    geo_midpoint: GeoCoordinates_Ref | list[GeoCoordinates_Ref] | None = Field(default=None, validation_alias="geoMidpoint", serialization_alias="geoMidpoint")
    geo_radius: Number_Text | list[Number_Text] | None = Field(default=None, validation_alias="geoRadius", serialization_alias="geoRadius")
