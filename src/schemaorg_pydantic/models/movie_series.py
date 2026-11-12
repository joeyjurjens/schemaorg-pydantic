from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .creative_work_series import CreativeWorkSeries

if TYPE_CHECKING:
    from .music_group import MusicGroup
    from .organization import Organization
    from .performing_group import PerformingGroup
    from .person import Person
    from .video_object import VideoObject

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


class MovieSeries(CreativeWorkSeries):
    """A series of movies. Included movies can be indicated with the hasPart property."""
    schema_type: ClassVar[str] = "MovieSeries"
    actor: PerformingGroup_Person_Ref | list[PerformingGroup_Person_Ref] | None = Field(default=None)
    director: Person_Ref | list[Person_Ref] | None = Field(default=None)
    music_by: MusicGroup_Person_Ref | list[MusicGroup_Person_Ref] | None = Field(default=None, validation_alias="musicBy", serialization_alias="musicBy")
    production_company: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="productionCompany", serialization_alias="productionCompany")
    trailer: VideoObject_Ref | list[VideoObject_Ref] | None = Field(default=None)
