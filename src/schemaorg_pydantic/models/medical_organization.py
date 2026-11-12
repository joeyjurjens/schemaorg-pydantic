from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Boolean, Text
from .organization import Organization
from .medical_specialty import MedicalSpecialty


class MedicalOrganization(Organization):
    """A medical organization (physical or not), such as hospital, institution or clinic."""
    schema_type: ClassVar[str] = "MedicalOrganization"
    health_plan_network_id: Text | list[Text] | None = Field(default=None, validation_alias="healthPlanNetworkId", serialization_alias="healthPlanNetworkId")
    is_accepting_new_patients: Boolean | list[Boolean] | None = Field(default=None, validation_alias="isAcceptingNewPatients", serialization_alias="isAcceptingNewPatients")
    medical_specialty: MedicalSpecialty | list[MedicalSpecialty] | None = Field(default=None, validation_alias="medicalSpecialty", serialization_alias="medicalSpecialty")
