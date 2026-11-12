from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Number, Ref, Text
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .creative_work_season import CreativeWorkSeason
    from .creative_work_series import CreativeWorkSeries
    from .episode import Episode
    from .hyper_toc_entry import HyperTocEntry
    from .music_group import MusicGroup
    from .performing_group import PerformingGroup
    from .person import Person

if TYPE_CHECKING:
    CreativeWorkSeason_Ref = Union[CreativeWorkSeason, Ref]
else:
    CreativeWorkSeason_Ref = Union[Is["CreativeWorkSeason"], Ref]

if TYPE_CHECKING:
    CreativeWorkSeries_Ref = Union[CreativeWorkSeries, Ref]
else:
    CreativeWorkSeries_Ref = Union[Is["CreativeWorkSeries"], Ref]

if TYPE_CHECKING:
    Episode_Ref = Union[Episode, Ref]
else:
    Episode_Ref = Union[Is["Episode"], Ref]

if TYPE_CHECKING:
    HyperTocEntry_Number_Ref = Union[HyperTocEntry, Number, Ref]
else:
    HyperTocEntry_Number_Ref = Union[Is["HyperTocEntry"], Number, Ref]

Integer_Text = Union[Integer, Text]
if TYPE_CHECKING:
    MusicGroup_Person_Ref = Union[MusicGroup, Person, Ref]
else:
    MusicGroup_Person_Ref = Union[Is["MusicGroup"], Is["Person"], Ref]

if TYPE_CHECKING:
    PerformingGroup_Person_Ref = Union[PerformingGroup, Person, Ref]
else:
    PerformingGroup_Person_Ref = Union[Is["PerformingGroup"], Is["Person"], Ref]

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]


class Clip(CreativeWork):
    """A short TV or radio program or a segment/part of a program."""
    schema_type: ClassVar[str] = "Clip"
    actor: PerformingGroup_Person_Ref | list[PerformingGroup_Person_Ref] | None = Field(default=None)
    clip_number: Integer_Text | list[Integer_Text] | None = Field(default=None, validation_alias="clipNumber", serialization_alias="clipNumber")
    director: Person_Ref | list[Person_Ref] | None = Field(default=None)
    end_offset: HyperTocEntry_Number_Ref | list[HyperTocEntry_Number_Ref] | None = Field(default=None, validation_alias="endOffset", serialization_alias="endOffset")
    music_by: MusicGroup_Person_Ref | list[MusicGroup_Person_Ref] | None = Field(default=None, validation_alias="musicBy", serialization_alias="musicBy")
    part_of_episode: Episode_Ref | list[Episode_Ref] | None = Field(default=None, validation_alias="partOfEpisode", serialization_alias="partOfEpisode")
    part_of_season: CreativeWorkSeason_Ref | list[CreativeWorkSeason_Ref] | None = Field(default=None, validation_alias="partOfSeason", serialization_alias="partOfSeason")
    part_of_series: CreativeWorkSeries_Ref | list[CreativeWorkSeries_Ref] | None = Field(default=None, validation_alias="partOfSeries", serialization_alias="partOfSeries")
    start_offset: HyperTocEntry_Number_Ref | list[HyperTocEntry_Number_Ref] | None = Field(default=None, validation_alias="startOffset", serialization_alias="startOffset")
