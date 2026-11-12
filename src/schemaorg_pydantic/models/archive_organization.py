from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .local_business import LocalBusiness

if TYPE_CHECKING:
    from .archive_component import ArchiveComponent

if TYPE_CHECKING:
    ArchiveComponent_Ref = Union[ArchiveComponent, Ref]
else:
    ArchiveComponent_Ref = Union[Is["ArchiveComponent"], Ref]


class ArchiveOrganization(LocalBusiness):
    """An organization with archival holdings. An organization which keeps and preserves archival material and typically makes it accessible to the public."""
    schema_type: ClassVar[str] = "ArchiveOrganization"
    archive_held: ArchiveComponent_Ref | list[ArchiveComponent_Ref] | None = Field(default=None, validation_alias="archiveHeld", serialization_alias="archiveHeld")
