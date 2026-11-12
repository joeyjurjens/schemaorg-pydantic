from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .create_action import CreateAction

if TYPE_CHECKING:
    from .food_establishment import FoodEstablishment
    from .food_event import FoodEvent
    from .place import Place
    from .recipe import Recipe

if TYPE_CHECKING:
    FoodEstablishment_Place_Ref = Union[FoodEstablishment, Place, Ref]
else:
    FoodEstablishment_Place_Ref = Union[Is["FoodEstablishment"], Is["Place"], Ref]

if TYPE_CHECKING:
    FoodEvent_Ref = Union[FoodEvent, Ref]
else:
    FoodEvent_Ref = Union[Is["FoodEvent"], Ref]

if TYPE_CHECKING:
    Recipe_Ref = Union[Recipe, Ref]
else:
    Recipe_Ref = Union[Is["Recipe"], Ref]


class CookAction(CreateAction):
    """The act of producing/preparing food."""
    schema_type: ClassVar[str] = "CookAction"
    food_establishment: FoodEstablishment_Place_Ref | list[FoodEstablishment_Place_Ref] | None = Field(default=None, validation_alias="foodEstablishment", serialization_alias="foodEstablishment")
    food_event: FoodEvent_Ref | list[FoodEvent_Ref] | None = Field(default=None, validation_alias="foodEvent", serialization_alias="foodEvent")
    recipe: Recipe_Ref | list[Recipe_Ref] | None = Field(default=None)
