from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .medical_entity import MedicalEntity

if TYPE_CHECKING:
    from .drug import Drug

if TYPE_CHECKING:
    Drug_Ref = Union[Drug, Ref]
else:
    Drug_Ref = Union[Is["Drug"], Ref]


class DrugClass(MedicalEntity):
    """A class of medical drugs, e.g., statins. Classes can represent general pharmacological class, common mechanisms of action, common physiological effects, etc."""
    schema_type: ClassVar[str] = "DrugClass"
    drug: Drug_Ref | list[Drug_Ref] | None = Field(default=None)
