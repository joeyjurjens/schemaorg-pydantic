from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .defined_term import DefinedTerm
    from .organization import Organization

if TYPE_CHECKING:
    AdministrativeArea_Ref = Union[AdministrativeArea, Ref]
else:
    AdministrativeArea_Ref = Union[Is["AdministrativeArea"], Ref]

if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]


class Credential(CreativeWork):
    """A credential is a certificate that is used to verify the identity of a person or entity."""
    schema_type: ClassVar[str] = "Credential"
    credential_category: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="credentialCategory", serialization_alias="credentialCategory")
    recognized_by: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="recognizedBy", serialization_alias="recognizedBy")
    valid_for: Text | list[Text] | None = Field(default=None, validation_alias="validFor", serialization_alias="validFor")
    valid_in: AdministrativeArea_Ref | list[AdministrativeArea_Ref] | None = Field(default=None, validation_alias="validIn", serialization_alias="validIn")
