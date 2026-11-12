from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .digital_document_permission import DigitalDocumentPermission

if TYPE_CHECKING:
    DigitalDocumentPermission_Ref = Union[DigitalDocumentPermission, Ref]
else:
    DigitalDocumentPermission_Ref = Union[Is["DigitalDocumentPermission"], Ref]


class DigitalDocument(CreativeWork):
    """An electronic file or document."""
    schema_type: ClassVar[str] = "DigitalDocument"
    has_digital_document_permission: DigitalDocumentPermission_Ref | list[DigitalDocumentPermission_Ref] | None = Field(default=None, validation_alias="hasDigitalDocumentPermission", serialization_alias="hasDigitalDocumentPermission")
