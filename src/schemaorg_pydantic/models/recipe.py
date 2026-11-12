from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .how_to import HowTo
from .restricted_diet import RestrictedDiet

if TYPE_CHECKING:
    from .creative_work import CreativeWork
    from .diet import Diet
    from .item_list import ItemList
    from .nutrition_information import NutritionInformation
    from .property_value import PropertyValue
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    CreativeWork_ItemList_Text_Ref = Union[CreativeWork, ItemList, Text, Ref]
else:
    CreativeWork_ItemList_Text_Ref = Union[Is["CreativeWork"], Is["ItemList"], Text, Ref]

if TYPE_CHECKING:
    Diet_RestrictedDiet_Ref = Union[Diet, RestrictedDiet, Ref]
else:
    Diet_RestrictedDiet_Ref = Union[Is["Diet"], RestrictedDiet, Ref]

if TYPE_CHECKING:
    ItemList_PropertyValue_Text_Ref = Union[ItemList, PropertyValue, Text, Ref]
else:
    ItemList_PropertyValue_Text_Ref = Union[Is["ItemList"], Is["PropertyValue"], Text, Ref]

if TYPE_CHECKING:
    NutritionInformation_Ref = Union[NutritionInformation, Ref]
else:
    NutritionInformation_Ref = Union[Is["NutritionInformation"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class Recipe(HowTo):
    """A recipe. For dietary restrictions covered by the recipe, a few common restrictions are enumerated via [[suitableForDiet]]. The [[keywords]] property can also be used to add more detail."""
    schema_type: ClassVar[str] = "Recipe"
    cook_time: Text | list[Text] | None = Field(default=None, validation_alias="cookTime", serialization_alias="cookTime")
    cooking_method: Text | list[Text] | None = Field(default=None, validation_alias="cookingMethod", serialization_alias="cookingMethod")
    nutrition: NutritionInformation_Ref | list[NutritionInformation_Ref] | None = Field(default=None)
    recipe_category: Text | list[Text] | None = Field(default=None, validation_alias="recipeCategory", serialization_alias="recipeCategory")
    recipe_cuisine: Text | list[Text] | None = Field(default=None, validation_alias="recipeCuisine", serialization_alias="recipeCuisine")
    recipe_ingredient: ItemList_PropertyValue_Text_Ref | list[ItemList_PropertyValue_Text_Ref] | None = Field(default=None, validation_alias="recipeIngredient", serialization_alias="recipeIngredient")
    recipe_instructions: CreativeWork_ItemList_Text_Ref | list[CreativeWork_ItemList_Text_Ref] | None = Field(default=None, validation_alias="recipeInstructions", serialization_alias="recipeInstructions")
    recipe_yield: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None, validation_alias="recipeYield", serialization_alias="recipeYield")
    suitable_for_diet: Diet_RestrictedDiet_Ref | list[Diet_RestrictedDiet_Ref] | None = Field(default=None, validation_alias="suitableForDiet", serialization_alias="suitableForDiet")
