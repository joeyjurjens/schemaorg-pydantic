from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text, Url
from .defined_term import DefinedTerm

if TYPE_CHECKING:
    from .category_code_set import CategoryCodeSet

if TYPE_CHECKING:
    CategoryCodeSet_Url_Ref = Union[CategoryCodeSet, Url, Ref]
else:
    CategoryCodeSet_Url_Ref = Union[Is["CategoryCodeSet"], Url, Ref]


class CategoryCode(DefinedTerm):
    """A Category Code."""
    schema_type: ClassVar[str] = "CategoryCode"
    code_value: Text | list[Text] | None = Field(default=None, validation_alias="codeValue", serialization_alias="codeValue")
    in_code_set: CategoryCodeSet_Url_Ref | list[CategoryCodeSet_Url_Ref] | None = Field(default=None, validation_alias="inCodeSet", serialization_alias="inCodeSet")
