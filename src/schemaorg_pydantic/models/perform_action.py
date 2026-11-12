from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .play_action import PlayAction

if TYPE_CHECKING:
    from .entertainment_business import EntertainmentBusiness

if TYPE_CHECKING:
    EntertainmentBusiness_Ref = Union[EntertainmentBusiness, Ref]
else:
    EntertainmentBusiness_Ref = Union[Is["EntertainmentBusiness"], Ref]


class PerformAction(PlayAction):
    """The act of participating in performance arts."""
    schema_type: ClassVar[str] = "PerformAction"
    entertainment_business: EntertainmentBusiness_Ref | list[EntertainmentBusiness_Ref] | None = Field(default=None, validation_alias="entertainmentBusiness", serialization_alias="entertainmentBusiness")
