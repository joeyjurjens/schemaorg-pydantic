from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Url
from .creative_work_series import CreativeWorkSeries

if TYPE_CHECKING:
    from .data_feed import DataFeed
    from .performing_group import PerformingGroup
    from .person import Person

if TYPE_CHECKING:
    DataFeed_Url_Ref = Union[DataFeed, Url, Ref]
else:
    DataFeed_Url_Ref = Union[Is["DataFeed"], Url, Ref]

if TYPE_CHECKING:
    PerformingGroup_Person_Ref = Union[PerformingGroup, Person, Ref]
else:
    PerformingGroup_Person_Ref = Union[Is["PerformingGroup"], Is["Person"], Ref]


class PodcastSeries(CreativeWorkSeries):
    """A podcast is an episodic series of digital audio or video files which a user can download and listen to."""
    schema_type: ClassVar[str] = "PodcastSeries"
    actor: PerformingGroup_Person_Ref | list[PerformingGroup_Person_Ref] | None = Field(default=None)
    web_feed: DataFeed_Url_Ref | list[DataFeed_Url_Ref] | None = Field(default=None, validation_alias="webFeed", serialization_alias="webFeed")
