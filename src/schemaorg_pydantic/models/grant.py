from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .intangible import Intangible

if TYPE_CHECKING:
    from .bio_chem_entity import BioChemEntity
    from .creative_work import CreativeWork
    from .event import Event
    from .medical_entity import MedicalEntity
    from .organization import Organization
    from .person import Person
    from .product import Product

if TYPE_CHECKING:
    R9b183bac = Union[BioChemEntity, CreativeWork, Event, MedicalEntity, Organization, Person, Product, Ref]
else:
    R9b183bac = Union[Is["BioChemEntity"], Is["CreativeWork"], Is["Event"], Is["MedicalEntity"], Is["Organization"], Is["Person"], Is["Product"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]


class Grant(Intangible):
    """A grant, typically financial or otherwise quantifiable, of resources. Typically a [[funder]] sponsors some [[MonetaryAmount]] to an [[Organization]] or [[Person]],\n    sometimes not necessarily via a dedicated or long-lived [[Project]], resulting in one or more outputs, or [[fundedItem]]s. For financial sponsorship, indicate the [[funder]] of a [[MonetaryGrant]]. For non-financial support, indicate [[sponsor]] of [[Grant]]s of resources (e.g. office space)."""
    schema_type: ClassVar[str] = "Grant"
    funded_item: R9b183bac | list[R9b183bac] | None = Field(default=None, validation_alias="fundedItem", serialization_alias="fundedItem")
    funder: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    sponsor: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
