from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .intangible import Intangible

if TYPE_CHECKING:
    from .offer import Offer
    from .organization import Organization

if TYPE_CHECKING:
    Offer_Ref = Union[Offer, Ref]
else:
    Offer_Ref = Union[Is["Offer"], Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]


class MediaSubscription(Intangible):
    """A subscription which allows a user to access media including audio, video, books, etc."""
    schema_type: ClassVar[str] = "MediaSubscription"
    authenticator: Organization_Ref | list[Organization_Ref] | None = Field(default=None)
    expects_acceptance_of: Offer_Ref | list[Offer_Ref] | None = Field(default=None, validation_alias="expectsAcceptanceOf", serialization_alias="expectsAcceptanceOf")
