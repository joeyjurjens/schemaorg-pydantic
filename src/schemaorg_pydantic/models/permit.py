from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Is, Ref, Text
from .intangible import Intangible

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .audience import Audience
    from .organization import Organization
    from .service import Service

if TYPE_CHECKING:
    AdministrativeArea_Ref = Union[AdministrativeArea, Ref]
else:
    AdministrativeArea_Ref = Union[Is["AdministrativeArea"], Ref]

if TYPE_CHECKING:
    Audience_Ref = Union[Audience, Ref]
else:
    Audience_Ref = Union[Is["Audience"], Ref]

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]

if TYPE_CHECKING:
    Service_Ref = Union[Service, Ref]
else:
    Service_Ref = Union[Is["Service"], Ref]


class Permit(Intangible):
    """A permit issued by an organization, e.g. a parking pass."""
    schema_type: ClassVar[str] = "Permit"
    issued_by: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="issuedBy", serialization_alias="issuedBy")
    issued_through: Service_Ref | list[Service_Ref] | None = Field(default=None, validation_alias="issuedThrough", serialization_alias="issuedThrough")
    permit_audience: Audience_Ref | list[Audience_Ref] | None = Field(default=None, validation_alias="permitAudience", serialization_alias="permitAudience")
    valid_for: Text | list[Text] | None = Field(default=None, validation_alias="validFor", serialization_alias="validFor")
    valid_from: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validFrom", serialization_alias="validFrom")
    valid_in: AdministrativeArea_Ref | list[AdministrativeArea_Ref] | None = Field(default=None, validation_alias="validIn", serialization_alias="validIn")
    valid_until: Date | list[Date] | None = Field(default=None, validation_alias="validUntil", serialization_alias="validUntil")
