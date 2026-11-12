from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .medical_condition import MedicalCondition
from .infectious_agent_class import InfectiousAgentClass


class InfectiousDisease(MedicalCondition):
    """An infectious disease is a clinically evident human disease resulting from the presence of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi, protozoa, multicellular parasites, and prions. To be considered an infectious disease, such pathogens are known to be able to cause this disease."""
    schema_type: ClassVar[str] = "InfectiousDisease"
    infectious_agent: Text | list[Text] | None = Field(default=None, validation_alias="infectiousAgent", serialization_alias="infectiousAgent")
    infectious_agent_class: InfectiousAgentClass | list[InfectiousAgentClass] | None = Field(default=None, validation_alias="infectiousAgentClass", serialization_alias="infectiousAgentClass")
    transmission_method: Text | list[Text] | None = Field(default=None, validation_alias="transmissionMethod", serialization_alias="transmissionMethod")
