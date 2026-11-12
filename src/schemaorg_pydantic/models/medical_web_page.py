from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .web_page import WebPage
from .medical_audience_type import MedicalAudienceType

if TYPE_CHECKING:
    from .medical_audience import MedicalAudience

if TYPE_CHECKING:
    MedicalAudience_MedicalAudienceType_Ref = Union[MedicalAudience, MedicalAudienceType, Ref]
else:
    MedicalAudience_MedicalAudienceType_Ref = Union[Is["MedicalAudience"], MedicalAudienceType, Ref]


class MedicalWebPage(WebPage):
    """A web page that provides medical information."""
    schema_type: ClassVar[str] = "MedicalWebPage"
    medical_audience: MedicalAudience_MedicalAudienceType_Ref | list[MedicalAudience_MedicalAudienceType_Ref] | None = Field(default=None, validation_alias="medicalAudience", serialization_alias="medicalAudience")
