from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref, Text
from .creative_work_series import CreativeWorkSeries

if TYPE_CHECKING:
    from .creative_work_season import CreativeWorkSeason
    from .episode import Episode
    from .music_group import MusicGroup
    from .organization import Organization
    from .performing_group import PerformingGroup
    from .person import Person
    from .video_object import VideoObject

if TYPE_CHECKING:
    CreativeWorkSeason_Ref = Union[CreativeWorkSeason, Ref]
else:
    CreativeWorkSeason_Ref = Union[Is["CreativeWorkSeason"], Ref]

if TYPE_CHECKING:
    Episode_Ref = Union[Episode, Ref]
else:
    Episode_Ref = Union[Is["Episode"], Ref]

if TYPE_CHECKING:
    MusicGroup_Person_Ref = Union[MusicGroup, Person, Ref]
else:
    MusicGroup_Person_Ref = Union[Is["MusicGroup"], Is["Person"], Ref]

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


class TVSeries(CreativeWorkSeries):
    """CreativeWorkSeries dedicated to TV broadcast and associated online delivery."""
    schema_type: ClassVar[str] = "TVSeries"
    actor: PerformingGroup_Person_Ref | list[PerformingGroup_Person_Ref] | None = Field(default=None)
    contains_season: CreativeWorkSeason_Ref | list[CreativeWorkSeason_Ref] | None = Field(default=None, validation_alias="containsSeason", serialization_alias="containsSeason")
    director: Person_Ref | list[Person_Ref] | None = Field(default=None)
    episode: Episode_Ref | list[Episode_Ref] | None = Field(default=None)
    music_by: MusicGroup_Person_Ref | list[MusicGroup_Person_Ref] | None = Field(default=None, validation_alias="musicBy", serialization_alias="musicBy")
    number_of_episodes: Integer | list[Integer] | None = Field(default=None, validation_alias="numberOfEpisodes", serialization_alias="numberOfEpisodes")
    number_of_seasons: Integer | list[Integer] | None = Field(default=None, validation_alias="numberOfSeasons", serialization_alias="numberOfSeasons")
    production_company: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="productionCompany", serialization_alias="productionCompany")
    title_eidr: Text | list[Text] | None = Field(default=None, validation_alias="titleEIDR", serialization_alias="titleEIDR")
    trailer: VideoObject_Ref | list[VideoObject_Ref] | None = Field(default=None)
