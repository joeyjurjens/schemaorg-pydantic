from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .online_store import OnlineStore

if TYPE_CHECKING:
    OnlineStore_Ref = Union[OnlineStore, Ref]
else:
    OnlineStore_Ref = Union[Is["OnlineStore"], Ref]


class OnlineMarketplace(OnlineStore):
    """An eCommerce marketplace."""
    schema_type: ClassVar[str] = "OnlineMarketplace"
    has_store: OnlineStore_Ref | list[OnlineStore_Ref] | None = Field(default=None, validation_alias="hasStore", serialization_alias="hasStore")
