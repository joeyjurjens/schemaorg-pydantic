from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .archive_organization import ArchiveOrganization
    from .place import Place
    from .postal_address import PostalAddress

if TYPE_CHECKING:
    ArchiveOrganization_Ref = Union[ArchiveOrganization, Ref]
else:
    ArchiveOrganization_Ref = Union[Is["ArchiveOrganization"], Ref]

if TYPE_CHECKING:
    Place_PostalAddress_Text_Ref = Union[Place, PostalAddress, Text, Ref]
else:
    Place_PostalAddress_Text_Ref = Union[Is["Place"], Is["PostalAddress"], Text, Ref]


class ArchiveComponent(CreativeWork):
    """An intangible type to be applied to any archive content, carrying with it a set of properties required to describe archival items and collections."""
    schema_type: ClassVar[str] = "ArchiveComponent"
    holding_archive: ArchiveOrganization_Ref | list[ArchiveOrganization_Ref] | None = Field(default=None, validation_alias="holdingArchive", serialization_alias="holdingArchive")
    item_location: Place_PostalAddress_Text_Ref | list[Place_PostalAddress_Text_Ref] | None = Field(default=None, validation_alias="itemLocation", serialization_alias="itemLocation")
