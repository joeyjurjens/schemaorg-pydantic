from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .transfer_action import TransferAction

if TYPE_CHECKING:
    from .audience import Audience
    from .contact_point import ContactPoint
    from .organization import Organization
    from .person import Person
    from .price_specification import PriceSpecification

if TYPE_CHECKING:
    R5c65ac19 = Union[Audience, ContactPoint, Organization, Person, Ref]
else:
    R5c65ac19 = Union[Is["Audience"], Is["ContactPoint"], Is["Organization"], Is["Person"], Ref]

Number_Text = Union[Number, Text]
if TYPE_CHECKING:
    PriceSpecification_Ref = Union[PriceSpecification, Ref]
else:
    PriceSpecification_Ref = Union[Is["PriceSpecification"], Ref]


class DonateAction(TransferAction):
    """The act of providing goods, services, or money without compensation, often for philanthropic reasons."""
    schema_type: ClassVar[str] = "DonateAction"
    price: Number_Text | list[Number_Text] | None = Field(default=None)
    price_currency: Text | list[Text] | None = Field(default=None, validation_alias="priceCurrency", serialization_alias="priceCurrency")
    price_specification: PriceSpecification_Ref | list[PriceSpecification_Ref] | None = Field(default=None, validation_alias="priceSpecification", serialization_alias="priceSpecification")
    recipient: R5c65ac19 | list[R5c65ac19] | None = Field(default=None)
