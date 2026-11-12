from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .intangible import Intangible

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea

if TYPE_CHECKING:
    AdministrativeArea_Ref = Union[AdministrativeArea, Ref]
else:
    AdministrativeArea_Ref = Union[Is["AdministrativeArea"], Ref]


class Audience(Intangible):
    """Intended audience for an item, i.e. the group for whom the item was created."""
    schema_type: ClassVar[str] = "Audience"
    audience_type: Text | list[Text] | None = Field(default=None, validation_alias="audienceType", serialization_alias="audienceType")
    geographic_area: AdministrativeArea_Ref | list[AdministrativeArea_Ref] | None = Field(default=None, validation_alias="geographicArea", serialization_alias="geographicArea")
