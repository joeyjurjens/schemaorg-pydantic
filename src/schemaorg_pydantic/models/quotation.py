from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]


class Quotation(CreativeWork):
    """A quotation. Often but not necessarily from some written work, attributable to a real world author and - if associated with a fictional character - to any fictional Person. Use [[isBasedOn]] to link to source/origin. The [[recordedIn]] property can be used to reference a Quotation from an [[Event]]."""
    schema_type: ClassVar[str] = "Quotation"
    spoken_by_character: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="spokenByCharacter", serialization_alias="spokenByCharacter")
