from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text, Url
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .data_feed import DataFeed
    from .image_object import ImageObject
    from .operating_system import OperatingSystem
    from .runtime_platform import RuntimePlatform

if TYPE_CHECKING:
    CreativeWork_Ref = Union[CreativeWork, Ref]
else:
    CreativeWork_Ref = Union[Is["CreativeWork"], Ref]

if TYPE_CHECKING:
    DataFeed_Ref = Union[DataFeed, Ref]
else:
    DataFeed_Ref = Union[Is["DataFeed"], Ref]

if TYPE_CHECKING:
    ImageObject_Url_Ref = Union[ImageObject, Url, Ref]
else:
    ImageObject_Url_Ref = Union[Is["ImageObject"], Url, Ref]

if TYPE_CHECKING:
    OperatingSystem_Text_Ref = Union[OperatingSystem, Text, Ref]
else:
    OperatingSystem_Text_Ref = Union[Is["OperatingSystem"], Text, Ref]

if TYPE_CHECKING:
    RuntimePlatform_Text_Ref = Union[RuntimePlatform, Text, Ref]
else:
    RuntimePlatform_Text_Ref = Union[Is["RuntimePlatform"], Text, Ref]

if TYPE_CHECKING:
    SoftwareApplication_Ref = Union["SoftwareApplication", Ref]
else:
    SoftwareApplication_Ref = Union[Is["SoftwareApplication"], Ref]

if TYPE_CHECKING:
    SoftwareApplication_Text_Ref = Union["SoftwareApplication", Text, Ref]
else:
    SoftwareApplication_Text_Ref = Union[Is["SoftwareApplication"], Text, Ref]


class SoftwareApplication(CreativeWork):
    """A software application."""
    schema_type: ClassVar[str] = "SoftwareApplication"
    application_category: Text | list[Text] | None = Field(default=None, validation_alias="applicationCategory", serialization_alias="applicationCategory")
    application_sub_category: Text | list[Text] | None = Field(default=None, validation_alias="applicationSubCategory", serialization_alias="applicationSubCategory")
    application_suite: Text | list[Text] | None = Field(default=None, validation_alias="applicationSuite", serialization_alias="applicationSuite")
    available_on_device: Text | list[Text] | None = Field(default=None, validation_alias="availableOnDevice", serialization_alias="availableOnDevice")
    countries_not_supported: Text | list[Text] | None = Field(default=None, validation_alias="countriesNotSupported", serialization_alias="countriesNotSupported")
    countries_supported: Text | list[Text] | None = Field(default=None, validation_alias="countriesSupported", serialization_alias="countriesSupported")
    download_url: Url | list[Url] | None = Field(default=None, validation_alias="downloadUrl", serialization_alias="downloadUrl")
    feature_list: Text | list[Text] | None = Field(default=None, validation_alias="featureList", serialization_alias="featureList")
    file_size: Text | list[Text] | None = Field(default=None, validation_alias="fileSize", serialization_alias="fileSize")
    install_url: Url | list[Url] | None = Field(default=None, validation_alias="installUrl", serialization_alias="installUrl")
    memory_requirements: Text | list[Text] | None = Field(default=None, validation_alias="memoryRequirements", serialization_alias="memoryRequirements")
    operating_system: OperatingSystem_Text_Ref | list[OperatingSystem_Text_Ref] | None = Field(default=None, validation_alias="operatingSystem", serialization_alias="operatingSystem")
    permissions: Text | list[Text] | None = Field(default=None)
    processor_requirements: Text | list[Text] | None = Field(default=None, validation_alias="processorRequirements", serialization_alias="processorRequirements")
    release_notes: Text | list[Text] | None = Field(default=None, validation_alias="releaseNotes", serialization_alias="releaseNotes")
    runtime_platform: RuntimePlatform_Text_Ref | list[RuntimePlatform_Text_Ref] | None = Field(default=None, validation_alias="runtimePlatform", serialization_alias="runtimePlatform")
    screenshot: ImageObject_Url_Ref | list[ImageObject_Url_Ref] | None = Field(default=None)
    software_add_on: SoftwareApplication_Ref | list[SoftwareApplication_Ref] | None = Field(default=None, validation_alias="softwareAddOn", serialization_alias="softwareAddOn")
    software_help: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="softwareHelp", serialization_alias="softwareHelp")
    software_requirements: SoftwareApplication_Text_Ref | list[SoftwareApplication_Text_Ref] | None = Field(default=None, validation_alias="softwareRequirements", serialization_alias="softwareRequirements")
    software_version: Text | list[Text] | None = Field(default=None, validation_alias="softwareVersion", serialization_alias="softwareVersion")
    storage_requirements: Text | list[Text] | None = Field(default=None, validation_alias="storageRequirements", serialization_alias="storageRequirements")
    supporting_data: DataFeed_Ref | list[DataFeed_Ref] | None = Field(default=None, validation_alias="supportingData", serialization_alias="supportingData")
