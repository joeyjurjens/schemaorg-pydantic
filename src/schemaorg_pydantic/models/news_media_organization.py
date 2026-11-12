from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Url
from .organization import Organization

if TYPE_CHECKING:
    from .creative_work import CreativeWork

if TYPE_CHECKING:
    CreativeWork_Url_Ref = Union[CreativeWork, Url, Ref]
else:
    CreativeWork_Url_Ref = Union[Is["CreativeWork"], Url, Ref]


class NewsMediaOrganization(Organization):
    """A News/Media organization such as a newspaper or TV station."""
    schema_type: ClassVar[str] = "NewsMediaOrganization"
    masthead: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None)
    mission_coverage_priorities_policy: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="missionCoveragePrioritiesPolicy", serialization_alias="missionCoveragePrioritiesPolicy")
    no_bylines_policy: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="noBylinesPolicy", serialization_alias="noBylinesPolicy")
    verification_fact_checking_policy: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="verificationFactCheckingPolicy", serialization_alias="verificationFactCheckingPolicy")
