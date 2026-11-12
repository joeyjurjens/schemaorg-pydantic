from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .interact_action import InteractAction

if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]


class FollowAction(InteractAction):
    """The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates polled from."""
    schema_type: ClassVar[str] = "FollowAction"
    followee: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
