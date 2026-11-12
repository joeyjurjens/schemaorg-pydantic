from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .service import Service

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .organization import Organization

if TYPE_CHECKING:
    AdministrativeArea_Text_Ref = Union[AdministrativeArea, Text, Ref]
else:
    AdministrativeArea_Text_Ref = Union[Is["AdministrativeArea"], Text, Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]


class GovernmentService(Service):
    """A service provided by a government organization, e.g. food stamps, veterans benefits, etc."""
    schema_type: ClassVar[str] = "GovernmentService"
    jurisdiction: AdministrativeArea_Text_Ref | list[AdministrativeArea_Text_Ref] | None = Field(default=None)
    service_operator: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="serviceOperator", serialization_alias="serviceOperator")
