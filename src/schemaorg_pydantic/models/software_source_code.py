from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text, Url
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .computer_language import ComputerLanguage
    from .runtime_platform import RuntimePlatform
    from .software_application import SoftwareApplication

if TYPE_CHECKING:
    ComputerLanguage_Text_Ref = Union[ComputerLanguage, Text, Ref]
else:
    ComputerLanguage_Text_Ref = Union[Is["ComputerLanguage"], Text, Ref]

if TYPE_CHECKING:
    RuntimePlatform_Text_Ref = Union[RuntimePlatform, Text, Ref]
else:
    RuntimePlatform_Text_Ref = Union[Is["RuntimePlatform"], Text, Ref]

if TYPE_CHECKING:
    SoftwareApplication_Ref = Union[SoftwareApplication, Ref]
else:
    SoftwareApplication_Ref = Union[Is["SoftwareApplication"], Ref]


class SoftwareSourceCode(CreativeWork):
    """Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates."""
    schema_type: ClassVar[str] = "SoftwareSourceCode"
    code_repository: Url | list[Url] | None = Field(default=None, validation_alias="codeRepository", serialization_alias="codeRepository")
    code_sample_type: Text | list[Text] | None = Field(default=None, validation_alias="codeSampleType", serialization_alias="codeSampleType")
    programming_language: ComputerLanguage_Text_Ref | list[ComputerLanguage_Text_Ref] | None = Field(default=None, validation_alias="programmingLanguage", serialization_alias="programmingLanguage")
    runtime_platform: RuntimePlatform_Text_Ref | list[RuntimePlatform_Text_Ref] | None = Field(default=None, validation_alias="runtimePlatform", serialization_alias="runtimePlatform")
    target_product: SoftwareApplication_Ref | list[SoftwareApplication_Ref] | None = Field(default=None, validation_alias="targetProduct", serialization_alias="targetProduct")
