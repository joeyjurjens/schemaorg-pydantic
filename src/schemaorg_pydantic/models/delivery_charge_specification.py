from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .price_specification import PriceSpecification
from .delivery_method import DeliveryMethod

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .geo_shape import GeoShape
    from .place import Place

if TYPE_CHECKING:
    R3fcc4ec8 = Union[AdministrativeArea, GeoShape, Place, Text, Ref]
else:
    R3fcc4ec8 = Union[Is["AdministrativeArea"], Is["GeoShape"], Is["Place"], Text, Ref]

if TYPE_CHECKING:
    GeoShape_Place_Text_Ref = Union[GeoShape, Place, Text, Ref]
else:
    GeoShape_Place_Text_Ref = Union[Is["GeoShape"], Is["Place"], Text, Ref]


class DeliveryChargeSpecification(PriceSpecification):
    """The price for the delivery of an offer using a particular delivery method."""
    schema_type: ClassVar[str] = "DeliveryChargeSpecification"
    applies_to_delivery_method: DeliveryMethod | list[DeliveryMethod] | None = Field(default=None, validation_alias="appliesToDeliveryMethod", serialization_alias="appliesToDeliveryMethod")
    area_served: R3fcc4ec8 | list[R3fcc4ec8] | None = Field(default=None, validation_alias="areaServed", serialization_alias="areaServed")
    eligible_region: GeoShape_Place_Text_Ref | list[GeoShape_Place_Text_Ref] | None = Field(default=None, validation_alias="eligibleRegion", serialization_alias="eligibleRegion")
    ineligible_region: GeoShape_Place_Text_Ref | list[GeoShape_Place_Text_Ref] | None = Field(default=None, validation_alias="ineligibleRegion", serialization_alias="ineligibleRegion")
