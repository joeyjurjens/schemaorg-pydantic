from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .credential import Credential

if TYPE_CHECKING:
    from .defined_term import DefinedTerm

if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]


class EducationalOccupationalCredential(Credential):
    """An educational or occupational credential. A diploma, academic degree, certification, qualification, badge, etc., that may be awarded to a person or other entity that meets the requirements defined by the credentialer."""
    schema_type: ClassVar[str] = "EducationalOccupationalCredential"
    competency_required: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="competencyRequired", serialization_alias="competencyRequired")
