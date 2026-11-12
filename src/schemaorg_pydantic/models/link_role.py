from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .role import Role

if TYPE_CHECKING:
    from .language import Language

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]


class LinkRole(Role):
    """A Role that represents a Web link, e.g. as expressed via the 'url' property. Its linkRelationship property can indicate URL-based and plain textual link types, e.g. those in IANA link registry or others such as 'amphtml'. This structure provides a placeholder where details from HTML's link element can be represented outside of HTML, e.g. in JSON-LD feeds."""
    schema_type: ClassVar[str] = "LinkRole"
    in_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="inLanguage", serialization_alias="inLanguage")
    link_relationship: Text | list[Text] | None = Field(default=None, validation_alias="linkRelationship", serialization_alias="linkRelationship")
