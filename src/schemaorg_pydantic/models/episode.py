from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref, Text
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .creative_work_season import CreativeWorkSeason
    from .creative_work_series import CreativeWorkSeries
    from .music_group import MusicGroup
    from .organization import Organization
    from .performing_group import PerformingGroup
    from .person import Person
    from .quantitative_value import QuantitativeValue
    from .video_object import VideoObject

if TYPE_CHECKING:
    CreativeWorkSeason_Ref = Union[CreativeWorkSeason, Ref]
else:
    CreativeWorkSeason_Ref = Union[Is["CreativeWorkSeason"], Ref]

if TYPE_CHECKING:
    CreativeWorkSeries_Ref = Union[CreativeWorkSeries, Ref]
else:
    CreativeWorkSeries_Ref = Union[Is["CreativeWorkSeries"], Ref]

Integer_Text = Union[Integer, Text]
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
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]

if TYPE_CHECKING:
    VideoObject_Ref = Union[VideoObject, Ref]
else:
    VideoObject_Ref = Union[Is["VideoObject"], Ref]


class Episode(CreativeWork):
    """A media episode (e.g. TV, radio, video game) which can be part of a series or season."""
    schema_type: ClassVar[str] = "Episode"
    actor: PerformingGroup_Person_Ref | list[PerformingGroup_Person_Ref] | None = Field(default=None)
    director: Person_Ref | list[Person_Ref] | None = Field(default=None)
    duration: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    episode_number: Integer_Text | list[Integer_Text] | None = Field(default=None, validation_alias="episodeNumber", serialization_alias="episodeNumber")
    music_by: MusicGroup_Person_Ref | list[MusicGroup_Person_Ref] | None = Field(default=None, validation_alias="musicBy", serialization_alias="musicBy")
    part_of_season: CreativeWorkSeason_Ref | list[CreativeWorkSeason_Ref] | None = Field(default=None, validation_alias="partOfSeason", serialization_alias="partOfSeason")
    part_of_series: CreativeWorkSeries_Ref | list[CreativeWorkSeries_Ref] | None = Field(default=None, validation_alias="partOfSeries", serialization_alias="partOfSeries")
    production_company: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="productionCompany", serialization_alias="productionCompany")
    trailer: VideoObject_Ref | list[VideoObject_Ref] | None = Field(default=None)
