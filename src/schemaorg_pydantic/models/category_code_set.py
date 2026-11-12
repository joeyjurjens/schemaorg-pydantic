from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .defined_term_set import DefinedTermSet

if TYPE_CHECKING:
    from .category_code import CategoryCode

if TYPE_CHECKING:
    CategoryCode_Ref = Union[CategoryCode, Ref]
else:
    CategoryCode_Ref = Union[Is["CategoryCode"], Ref]


class CategoryCodeSet(DefinedTermSet):
    """A set of Category Code values."""
    schema_type: ClassVar[str] = "CategoryCodeSet"
    has_category_code: CategoryCode_Ref | list[CategoryCode_Ref] | None = Field(default=None, validation_alias="hasCategoryCode", serialization_alias="hasCategoryCode")
