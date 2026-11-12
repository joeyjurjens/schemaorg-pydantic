from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .react_action import ReactAction

if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]


class EndorseAction(ReactAction):
    """An agent approves/certifies/likes/supports/sanctions an object."""
    schema_type: ClassVar[str] = "EndorseAction"
    endorsee: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
