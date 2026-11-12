from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .transfer_action import TransferAction
from .delivery_method import DeliveryMethod

if TYPE_CHECKING:
    from .audience import Audience
    from .contact_point import ContactPoint
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    R5c65ac19 = Union[Audience, ContactPoint, Organization, Person, Ref]
else:
    R5c65ac19 = Union[Is["Audience"], Is["ContactPoint"], Is["Organization"], Is["Person"], Ref]


class SendAction(TransferAction):
    """The act of physically/electronically dispatching an object for transfer from an origin to a destination. Related actions:"""
    schema_type: ClassVar[str] = "SendAction"
    delivery_method: DeliveryMethod | list[DeliveryMethod] | None = Field(default=None, validation_alias="deliveryMethod", serialization_alias="deliveryMethod")
    recipient: R5c65ac19 | list[R5c65ac19] | None = Field(default=None)
