from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .defined_term import DefinedTerm

if TYPE_CHECKING:
    DefinedTerm_Ref = Union[DefinedTerm, Ref]
else:
    DefinedTerm_Ref = Union[Is["DefinedTerm"], Ref]


class DefinedTermSet(CreativeWork):
    """A set of defined terms, for example a set of categories or a classification scheme, a glossary, dictionary or enumeration. Use the about property to specify what the term set is about."""
    schema_type: ClassVar[str] = "DefinedTermSet"
    has_defined_term: DefinedTerm_Ref | list[DefinedTerm_Ref] | None = Field(default=None, validation_alias="hasDefinedTerm", serialization_alias="hasDefinedTerm")
