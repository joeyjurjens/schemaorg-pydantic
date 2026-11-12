from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Integer, Is, Ref, Text
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .creative_work_series import CreativeWorkSeries
    from .episode import Episode
    from .organization import Organization
    from .performing_group import PerformingGroup
    from .person import Person
    from .video_object import VideoObject

if TYPE_CHECKING:
    CreativeWorkSeries_Ref = Union[CreativeWorkSeries, Ref]
else:
    CreativeWorkSeries_Ref = Union[Is["CreativeWorkSeries"], Ref]

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    Episode_Ref = Union[Episode, Ref]
else:
    Episode_Ref = Union[Is["Episode"], Ref]

Integer_Text = Union[Integer, Text]
if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]

if TYPE_CHECKING:
    PerformingGroup_Person_Ref = Union[PerformingGroup, Person, Ref]
else:
    PerformingGroup_Person_Ref = Union[Is["PerformingGroup"], Is["Person"], Ref]

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]

if TYPE_CHECKING:
    VideoObject_Ref = Union[VideoObject, Ref]
else:
    VideoObject_Ref = Union[Is["VideoObject"], Ref]


class CreativeWorkSeason(CreativeWork):
    """A media season, e.g. TV, radio, video game etc."""
    schema_type: ClassVar[str] = "CreativeWorkSeason"
    actor: PerformingGroup_Person_Ref | list[PerformingGroup_Person_Ref] | None = Field(default=None)
    director: Person_Ref | list[Person_Ref] | None = Field(default=None)
    end_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="endDate", serialization_alias="endDate")
    episode: Episode_Ref | list[Episode_Ref] | None = Field(default=None)
    number_of_episodes: Integer | list[Integer] | None = Field(default=None, validation_alias="numberOfEpisodes", serialization_alias="numberOfEpisodes")
    part_of_series: CreativeWorkSeries_Ref | list[CreativeWorkSeries_Ref] | None = Field(default=None, validation_alias="partOfSeries", serialization_alias="partOfSeries")
    production_company: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="productionCompany", serialization_alias="productionCompany")
    season_number: Integer_Text | list[Integer_Text] | None = Field(default=None, validation_alias="seasonNumber", serialization_alias="seasonNumber")
    start_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="startDate", serialization_alias="startDate")
    trailer: VideoObject_Ref | list[VideoObject_Ref] | None = Field(default=None)
