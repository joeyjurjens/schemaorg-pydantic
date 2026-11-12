from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .trade_action import TradeAction

if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person
    from .real_estate_agent import RealEstateAgent

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    RealEstateAgent_Ref = Union[RealEstateAgent, Ref]
else:
    RealEstateAgent_Ref = Union[Is["RealEstateAgent"], Ref]


class RentAction(TradeAction):
    """The act of giving money in return for temporary use, but not ownership, of an object such as a vehicle or property. For example, an agent rents a property from a landlord in exchange for a periodic payment."""
    schema_type: ClassVar[str] = "RentAction"
    landlord: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    real_estate_agent: RealEstateAgent_Ref | list[RealEstateAgent_Ref] | None = Field(default=None, validation_alias="realEstateAgent", serialization_alias="realEstateAgent")
