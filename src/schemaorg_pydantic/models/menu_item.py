from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .intangible import Intangible
from .restricted_diet import RestrictedDiet

if TYPE_CHECKING:
    from .demand import Demand
    from .diet import Diet
    from .menu_section import MenuSection
    from .nutrition_information import NutritionInformation
    from .offer import Offer

if TYPE_CHECKING:
    Demand_Offer_Ref = Union[Demand, Offer, Ref]
else:
    Demand_Offer_Ref = Union[Is["Demand"], Is["Offer"], Ref]

if TYPE_CHECKING:
    Diet_RestrictedDiet_Ref = Union[Diet, RestrictedDiet, Ref]
else:
    Diet_RestrictedDiet_Ref = Union[Is["Diet"], RestrictedDiet, Ref]

if TYPE_CHECKING:
    MenuItem_MenuSection_Ref = Union["MenuItem", MenuSection, Ref]
else:
    MenuItem_MenuSection_Ref = Union[Is["MenuItem"], Is["MenuSection"], Ref]

if TYPE_CHECKING:
    NutritionInformation_Ref = Union[NutritionInformation, Ref]
else:
    NutritionInformation_Ref = Union[Is["NutritionInformation"], Ref]


class MenuItem(Intangible):
    """A food or drink item listed in a menu or menu section."""
    schema_type: ClassVar[str] = "MenuItem"
    menu_add_on: MenuItem_MenuSection_Ref | list[MenuItem_MenuSection_Ref] | None = Field(default=None, validation_alias="menuAddOn", serialization_alias="menuAddOn")
    nutrition: NutritionInformation_Ref | list[NutritionInformation_Ref] | None = Field(default=None)
    offers: Demand_Offer_Ref | list[Demand_Offer_Ref] | None = Field(default=None)
    suitable_for_diet: Diet_RestrictedDiet_Ref | list[Diet_RestrictedDiet_Ref] | None = Field(default=None, validation_alias="suitableForDiet", serialization_alias="suitableForDiet")
