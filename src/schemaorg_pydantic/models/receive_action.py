from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .transfer_action import TransferAction
from .delivery_method import DeliveryMethod

if TYPE_CHECKING:
    from .audience import Audience
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    Audience_Organization_Person_Ref = Union[Audience, Organization, Person, Ref]
else:
    Audience_Organization_Person_Ref = Union[Is["Audience"], Is["Organization"], Is["Person"], Ref]


class ReceiveAction(TransferAction):
    """The act of physically/electronically taking delivery of an object that has been transferred from an origin to a destination. Reciprocal of SendAction."""
    schema_type: ClassVar[str] = "ReceiveAction"
    delivery_method: DeliveryMethod | list[DeliveryMethod] | None = Field(default=None, validation_alias="deliveryMethod", serialization_alias="deliveryMethod")
    sender: Audience_Organization_Person_Ref | list[Audience_Organization_Person_Ref] | None = Field(default=None)
