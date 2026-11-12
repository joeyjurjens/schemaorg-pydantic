from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Date, DateTime, Is, Ref, Text, Time
from .intangible import Intangible
from .physical_activity_category import PhysicalActivityCategory

if TYPE_CHECKING:
    from .category_code import CategoryCode
    from .geo_shape import GeoShape
    from .media_subscription import MediaSubscription
    from .offer import Offer
    from .place import Place
    from .thing import Thing

if TYPE_CHECKING:
    R88d1e012 = Union[CategoryCode, PhysicalActivityCategory, Thing, Text, Ref]
else:
    R88d1e012 = Union[Is["CategoryCode"], PhysicalActivityCategory, Is["Thing"], Text, Ref]

Date_DateTime_Time = Union[Date, DateTime, Time]
if TYPE_CHECKING:
    GeoShape_Place_Text_Ref = Union[GeoShape, Place, Text, Ref]
else:
    GeoShape_Place_Text_Ref = Union[Is["GeoShape"], Is["Place"], Text, Ref]

if TYPE_CHECKING:
    MediaSubscription_Boolean_Ref = Union[MediaSubscription, Boolean, Ref]
else:
    MediaSubscription_Boolean_Ref = Union[Is["MediaSubscription"], Boolean, Ref]

if TYPE_CHECKING:
    Offer_Ref = Union[Offer, Ref]
else:
    Offer_Ref = Union[Is["Offer"], Ref]


class ActionAccessSpecification(Intangible):
    """A set of requirements that must be fulfilled in order to perform an Action."""
    schema_type: ClassVar[str] = "ActionAccessSpecification"
    availability_ends: Date_DateTime_Time | list[Date_DateTime_Time] | None = Field(default=None, validation_alias="availabilityEnds", serialization_alias="availabilityEnds")
    availability_starts: Date_DateTime_Time | list[Date_DateTime_Time] | None = Field(default=None, validation_alias="availabilityStarts", serialization_alias="availabilityStarts")
    category: R88d1e012 | list[R88d1e012] | None = Field(default=None)
    eligible_region: GeoShape_Place_Text_Ref | list[GeoShape_Place_Text_Ref] | None = Field(default=None, validation_alias="eligibleRegion", serialization_alias="eligibleRegion")
    expects_acceptance_of: Offer_Ref | list[Offer_Ref] | None = Field(default=None, validation_alias="expectsAcceptanceOf", serialization_alias="expectsAcceptanceOf")
    ineligible_region: GeoShape_Place_Text_Ref | list[GeoShape_Place_Text_Ref] | None = Field(default=None, validation_alias="ineligibleRegion", serialization_alias="ineligibleRegion")
    requires_subscription: MediaSubscription_Boolean_Ref | list[MediaSubscription_Boolean_Ref] | None = Field(default=None, validation_alias="requiresSubscription", serialization_alias="requiresSubscription")
