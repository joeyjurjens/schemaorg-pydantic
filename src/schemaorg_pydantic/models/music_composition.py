from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .event import Event
    from .music_recording import MusicRecording
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    CreativeWork_Ref = Union[CreativeWork, Ref]
else:
    CreativeWork_Ref = Union[Is["CreativeWork"], Ref]

if TYPE_CHECKING:
    Event_Ref = Union[Event, Ref]
else:
    Event_Ref = Union[Is["Event"], Ref]

if TYPE_CHECKING:
    MusicComposition_Ref = Union["MusicComposition", Ref]
else:
    MusicComposition_Ref = Union[Is["MusicComposition"], Ref]

if TYPE_CHECKING:
    MusicRecording_Ref = Union[MusicRecording, Ref]
else:
    MusicRecording_Ref = Union[Is["MusicRecording"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]


class MusicComposition(CreativeWork):
    """A musical composition."""
    schema_type: ClassVar[str] = "MusicComposition"
    composer: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    first_performance: Event_Ref | list[Event_Ref] | None = Field(default=None, validation_alias="firstPerformance", serialization_alias="firstPerformance")
    included_composition: MusicComposition_Ref | list[MusicComposition_Ref] | None = Field(default=None, validation_alias="includedComposition", serialization_alias="includedComposition")
    iswc_code: Text | list[Text] | None = Field(default=None, validation_alias="iswcCode", serialization_alias="iswcCode")
    lyricist: Person_Ref | list[Person_Ref] | None = Field(default=None)
    lyrics: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None)
    music_arrangement: MusicComposition_Ref | list[MusicComposition_Ref] | None = Field(default=None, validation_alias="musicArrangement", serialization_alias="musicArrangement")
    music_composition_form: Text | list[Text] | None = Field(default=None, validation_alias="musicCompositionForm", serialization_alias="musicCompositionForm")
    musical_key: Text | list[Text] | None = Field(default=None, validation_alias="musicalKey", serialization_alias="musicalKey")
    recorded_as: MusicRecording_Ref | list[MusicRecording_Ref] | None = Field(default=None, validation_alias="recordedAs", serialization_alias="recordedAs")
