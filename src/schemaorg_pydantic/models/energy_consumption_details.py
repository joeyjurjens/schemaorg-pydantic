from __future__ import annotations

from typing import ClassVar, Union

from pydantic import Field

from .intangible import Intangible
from .eu_energy_efficiency_enumeration import EUEnergyEfficiencyEnumeration
from .energy_star_energy_efficiency_enumeration import EnergyStarEnergyEfficiencyEnumeration

EUEnergyEfficiencyEnumeration_EnergyStarEnergyEfficiencyEnumeration = Union[EUEnergyEfficiencyEnumeration, EnergyStarEnergyEfficiencyEnumeration]

class EnergyConsumptionDetails(Intangible):
    """EnergyConsumptionDetails represents information related to the energy efficiency of a product that consumes energy. The information that can be provided is based on international regulations such as for example [EU directive 2017/1369](https://eur-lex.europa.eu/eli/reg/2017/1369/oj) for energy labeling and the [Energy labeling rule](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/energy-water-use-labeling-consumer) under the Energy Policy and Conservation Act (EPCA) in the US."""
    schema_type: ClassVar[str] = "EnergyConsumptionDetails"
    energy_efficiency_scale_max: EUEnergyEfficiencyEnumeration | list[EUEnergyEfficiencyEnumeration] | None = Field(default=None, validation_alias="energyEfficiencyScaleMax", serialization_alias="energyEfficiencyScaleMax")
    energy_efficiency_scale_min: EUEnergyEfficiencyEnumeration | list[EUEnergyEfficiencyEnumeration] | None = Field(default=None, validation_alias="energyEfficiencyScaleMin", serialization_alias="energyEfficiencyScaleMin")
    has_energy_efficiency_category: EUEnergyEfficiencyEnumeration_EnergyStarEnergyEfficiencyEnumeration | list[EUEnergyEfficiencyEnumeration_EnergyStarEnergyEfficiencyEnumeration] | None = Field(default=None, validation_alias="hasEnergyEfficiencyCategory", serialization_alias="hasEnergyEfficiencyCategory")
