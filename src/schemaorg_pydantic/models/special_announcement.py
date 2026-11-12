from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Is, Ref, Text, Url
from .creative_work import CreativeWork
from .physical_activity_category import PhysicalActivityCategory

if TYPE_CHECKING:
    from .category_code import CategoryCode
    from .civic_structure import CivicStructure
    from .data_feed import DataFeed
    from .dataset import Dataset
    from .government_service import GovernmentService
    from .local_business import LocalBusiness
    from .observation import Observation
    from .thing import Thing
    from .web_content import WebContent

if TYPE_CHECKING:
    R88d1e012 = Union[CategoryCode, PhysicalActivityCategory, Thing, Text, Ref]
else:
    R88d1e012 = Union[Is["CategoryCode"], PhysicalActivityCategory, Is["Thing"], Text, Ref]

if TYPE_CHECKING:
    CivicStructure_LocalBusiness_Ref = Union[CivicStructure, LocalBusiness, Ref]
else:
    CivicStructure_LocalBusiness_Ref = Union[Is["CivicStructure"], Is["LocalBusiness"], Ref]

if TYPE_CHECKING:
    DataFeed_Url_Ref = Union[DataFeed, Url, Ref]
else:
    DataFeed_Url_Ref = Union[Is["DataFeed"], Url, Ref]

if TYPE_CHECKING:
    R54831b56 = Union[Dataset, Observation, WebContent, Url, Ref]
else:
    R54831b56 = Union[Is["Dataset"], Is["Observation"], Is["WebContent"], Url, Ref]

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    GovernmentService_Ref = Union[GovernmentService, Ref]
else:
    GovernmentService_Ref = Union[Is["GovernmentService"], Ref]

if TYPE_CHECKING:
    WebContent_Url_Ref = Union[WebContent, Url, Ref]
else:
    WebContent_Url_Ref = Union[Is["WebContent"], Url, Ref]


class SpecialAnnouncement(CreativeWork):
    """A SpecialAnnouncement combines a simple date-stamped textual information update\n      with contextualized Web links and other structured data.  It represents an information update made by a\n      locally-oriented organization, for example schools, pharmacies, healthcare providers,  community groups, police,\n      local government."""
    schema_type: ClassVar[str] = "SpecialAnnouncement"
    announcement_location: CivicStructure_LocalBusiness_Ref | list[CivicStructure_LocalBusiness_Ref] | None = Field(default=None, validation_alias="announcementLocation", serialization_alias="announcementLocation")
    category: R88d1e012 | list[R88d1e012] | None = Field(default=None)
    date_posted: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="datePosted", serialization_alias="datePosted")
    disease_prevention_info: WebContent_Url_Ref | list[WebContent_Url_Ref] | None = Field(default=None, validation_alias="diseasePreventionInfo", serialization_alias="diseasePreventionInfo")
    disease_spread_statistics: R54831b56 | list[R54831b56] | None = Field(default=None, validation_alias="diseaseSpreadStatistics", serialization_alias="diseaseSpreadStatistics")
    getting_tested_info: WebContent_Url_Ref | list[WebContent_Url_Ref] | None = Field(default=None, validation_alias="gettingTestedInfo", serialization_alias="gettingTestedInfo")
    government_benefits_info: GovernmentService_Ref | list[GovernmentService_Ref] | None = Field(default=None, validation_alias="governmentBenefitsInfo", serialization_alias="governmentBenefitsInfo")
    news_updates_and_guidelines: WebContent_Url_Ref | list[WebContent_Url_Ref] | None = Field(default=None, validation_alias="newsUpdatesAndGuidelines", serialization_alias="newsUpdatesAndGuidelines")
    public_transport_closures_info: WebContent_Url_Ref | list[WebContent_Url_Ref] | None = Field(default=None, validation_alias="publicTransportClosuresInfo", serialization_alias="publicTransportClosuresInfo")
    quarantine_guidelines: WebContent_Url_Ref | list[WebContent_Url_Ref] | None = Field(default=None, validation_alias="quarantineGuidelines", serialization_alias="quarantineGuidelines")
    school_closures_info: WebContent_Url_Ref | list[WebContent_Url_Ref] | None = Field(default=None, validation_alias="schoolClosuresInfo", serialization_alias="schoolClosuresInfo")
    travel_bans: WebContent_Url_Ref | list[WebContent_Url_Ref] | None = Field(default=None, validation_alias="travelBans", serialization_alias="travelBans")
    web_feed: DataFeed_Url_Ref | list[DataFeed_Url_Ref] | None = Field(default=None, validation_alias="webFeed", serialization_alias="webFeed")
