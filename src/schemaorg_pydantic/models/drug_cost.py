from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .medical_entity import MedicalEntity
from .drive_wheel_configuration_value import DriveWheelConfigurationValue
from .drug_cost_category import DrugCostCategory
from .steering_position_value import SteeringPositionValue

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea

if TYPE_CHECKING:
    AdministrativeArea_Ref = Union[AdministrativeArea, Ref]
else:
    AdministrativeArea_Ref = Union[Is["AdministrativeArea"], Ref]

DriveWheelConfigurationValue_SteeringPositionValue_Number_Text = Union[DriveWheelConfigurationValue, SteeringPositionValue, Number, Text]

class DrugCost(MedicalEntity):
    """The cost per unit of a medical drug. Note that this type is not meant to represent the price in an offer of a drug for sale; see the Offer type for that. This type will typically be used to tag wholesale or average retail cost of a drug, or maximum reimbursable cost. Costs of medical drugs vary widely depending on how and where they are paid for, so while this type captures some of the variables, costs should be used with caution by consumers of this schema's markup."""
    schema_type: ClassVar[str] = "DrugCost"
    applicable_location: AdministrativeArea_Ref | list[AdministrativeArea_Ref] | None = Field(default=None, validation_alias="applicableLocation", serialization_alias="applicableLocation")
    cost_category: DrugCostCategory | list[DrugCostCategory] | None = Field(default=None, validation_alias="costCategory", serialization_alias="costCategory")
    cost_currency: Text | list[Text] | None = Field(default=None, validation_alias="costCurrency", serialization_alias="costCurrency")
    cost_origin: Text | list[Text] | None = Field(default=None, validation_alias="costOrigin", serialization_alias="costOrigin")
    cost_per_unit: DriveWheelConfigurationValue_SteeringPositionValue_Number_Text | list[DriveWheelConfigurationValue_SteeringPositionValue_Number_Text] | None = Field(default=None, validation_alias="costPerUnit", serialization_alias="costPerUnit")
    drug_unit: Text | list[Text] | None = Field(default=None, validation_alias="drugUnit", serialization_alias="drugUnit")
