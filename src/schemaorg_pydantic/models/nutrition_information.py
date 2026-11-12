from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .structured_value import StructuredValue


class NutritionInformation(StructuredValue):
    """Nutritional information about the recipe."""
    schema_type: ClassVar[str] = "NutritionInformation"
    calories: Text | list[Text] | None = Field(default=None)
    carbohydrate_content: Text | list[Text] | None = Field(default=None, validation_alias="carbohydrateContent", serialization_alias="carbohydrateContent")
    cholesterol_content: Text | list[Text] | None = Field(default=None, validation_alias="cholesterolContent", serialization_alias="cholesterolContent")
    fat_content: Text | list[Text] | None = Field(default=None, validation_alias="fatContent", serialization_alias="fatContent")
    fiber_content: Text | list[Text] | None = Field(default=None, validation_alias="fiberContent", serialization_alias="fiberContent")
    protein_content: Text | list[Text] | None = Field(default=None, validation_alias="proteinContent", serialization_alias="proteinContent")
    saturated_fat_content: Text | list[Text] | None = Field(default=None, validation_alias="saturatedFatContent", serialization_alias="saturatedFatContent")
    serving_size: Text | list[Text] | None = Field(default=None, validation_alias="servingSize", serialization_alias="servingSize")
    sodium_content: Text | list[Text] | None = Field(default=None, validation_alias="sodiumContent", serialization_alias="sodiumContent")
    sugar_content: Text | list[Text] | None = Field(default=None, validation_alias="sugarContent", serialization_alias="sugarContent")
    trans_fat_content: Text | list[Text] | None = Field(default=None, validation_alias="transFatContent", serialization_alias="transFatContent")
    unsaturated_fat_content: Text | list[Text] | None = Field(default=None, validation_alias="unsaturatedFatContent", serialization_alias="unsaturatedFatContent")
