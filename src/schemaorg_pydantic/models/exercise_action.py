from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .play_action import PlayAction

if TYPE_CHECKING:
    from .diet import Diet
    from .exercise_plan import ExercisePlan
    from .person import Person
    from .place import Place
    from .sports_activity_location import SportsActivityLocation
    from .sports_event import SportsEvent
    from .sports_team import SportsTeam

if TYPE_CHECKING:
    Diet_Ref = Union[Diet, Ref]
else:
    Diet_Ref = Union[Is["Diet"], Ref]

if TYPE_CHECKING:
    ExercisePlan_Ref = Union[ExercisePlan, Ref]
else:
    ExercisePlan_Ref = Union[Is["ExercisePlan"], Ref]

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]

if TYPE_CHECKING:
    Place_Ref = Union[Place, Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]

if TYPE_CHECKING:
    SportsActivityLocation_Ref = Union[SportsActivityLocation, Ref]
else:
    SportsActivityLocation_Ref = Union[Is["SportsActivityLocation"], Ref]

if TYPE_CHECKING:
    SportsEvent_Ref = Union[SportsEvent, Ref]
else:
    SportsEvent_Ref = Union[Is["SportsEvent"], Ref]

if TYPE_CHECKING:
    SportsTeam_Ref = Union[SportsTeam, Ref]
else:
    SportsTeam_Ref = Union[Is["SportsTeam"], Ref]


class ExerciseAction(PlayAction):
    """The act of participating in exertive activity for the purposes of improving health and fitness."""
    schema_type: ClassVar[str] = "ExerciseAction"
    diet: Diet_Ref | list[Diet_Ref] | None = Field(default=None)
    distance: Text | list[Text] | None = Field(default=None)
    exercise_course: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="exerciseCourse", serialization_alias="exerciseCourse")
    exercise_plan: ExercisePlan_Ref | list[ExercisePlan_Ref] | None = Field(default=None, validation_alias="exercisePlan", serialization_alias="exercisePlan")
    exercise_related_diet: Diet_Ref | list[Diet_Ref] | None = Field(default=None, validation_alias="exerciseRelatedDiet", serialization_alias="exerciseRelatedDiet")
    exercise_type: Text | list[Text] | None = Field(default=None, validation_alias="exerciseType", serialization_alias="exerciseType")
    from_location: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="fromLocation", serialization_alias="fromLocation")
    opponent: Person_Ref | list[Person_Ref] | None = Field(default=None)
    sports_activity_location: SportsActivityLocation_Ref | list[SportsActivityLocation_Ref] | None = Field(default=None, validation_alias="sportsActivityLocation", serialization_alias="sportsActivityLocation")
    sports_event: SportsEvent_Ref | list[SportsEvent_Ref] | None = Field(default=None, validation_alias="sportsEvent", serialization_alias="sportsEvent")
    sports_team: SportsTeam_Ref | list[SportsTeam_Ref] | None = Field(default=None, validation_alias="sportsTeam", serialization_alias="sportsTeam")
    to_location: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="toLocation", serialization_alias="toLocation")
