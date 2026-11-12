from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .intangible import Intangible
from .digital_document_permission_type import DigitalDocumentPermissionType

if TYPE_CHECKING:
    from .audience import Audience
    from .contact_point import ContactPoint
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    R5c65ac19 = Union[Audience, ContactPoint, Organization, Person, Ref]
else:
    R5c65ac19 = Union[Is["Audience"], Is["ContactPoint"], Is["Organization"], Is["Person"], Ref]


class DigitalDocumentPermission(Intangible):
    """A permission for a particular person or group to access a particular file."""
    schema_type: ClassVar[str] = "DigitalDocumentPermission"
    grantee: R5c65ac19 | list[R5c65ac19] | None = Field(default=None)
    permission_type: DigitalDocumentPermissionType | list[DigitalDocumentPermissionType] | None = Field(default=None, validation_alias="permissionType", serialization_alias="permissionType")
