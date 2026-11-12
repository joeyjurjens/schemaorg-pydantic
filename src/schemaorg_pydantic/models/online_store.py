from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .online_business import OnlineBusiness

if TYPE_CHECKING:
    from .online_marketplace import OnlineMarketplace

if TYPE_CHECKING:
    OnlineMarketplace_Ref = Union[OnlineMarketplace, Ref]
else:
    OnlineMarketplace_Ref = Union[Is["OnlineMarketplace"], Ref]


class OnlineStore(OnlineBusiness):
    """An eCommerce site."""
    schema_type: ClassVar[str] = "OnlineStore"
    is_store_on: OnlineMarketplace_Ref | list[OnlineMarketplace_Ref] | None = Field(default=None, validation_alias="isStoreOn", serialization_alias="isStoreOn")
