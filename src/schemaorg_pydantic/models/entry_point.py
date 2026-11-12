from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .intangible import Intangible
from .digital_platform_enumeration import DigitalPlatformEnumeration

if TYPE_CHECKING:
    from .software_application import SoftwareApplication

DigitalPlatformEnumeration_Text = Union[DigitalPlatformEnumeration, Text]
if TYPE_CHECKING:
    SoftwareApplication_Ref = Union[SoftwareApplication, Ref]
else:
    SoftwareApplication_Ref = Union[Is["SoftwareApplication"], Ref]


class EntryPoint(Intangible):
    """An entry point, within some Web-based protocol."""
    schema_type: ClassVar[str] = "EntryPoint"
    action_application: SoftwareApplication_Ref | list[SoftwareApplication_Ref] | None = Field(default=None, validation_alias="actionApplication", serialization_alias="actionApplication")
    action_platform: DigitalPlatformEnumeration_Text | list[DigitalPlatformEnumeration_Text] | None = Field(default=None, validation_alias="actionPlatform", serialization_alias="actionPlatform")
    content_type: Text | list[Text] | None = Field(default=None, validation_alias="contentType", serialization_alias="contentType")
    encoding_type: Text | list[Text] | None = Field(default=None, validation_alias="encodingType", serialization_alias="encodingType")
    http_method: Text | list[Text] | None = Field(default=None, validation_alias="httpMethod", serialization_alias="httpMethod")
    url_template: Text | list[Text] | None = Field(default=None, validation_alias="urlTemplate", serialization_alias="urlTemplate")
