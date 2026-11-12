from __future__ import annotations

from typing import ClassVar, Union

from pydantic import Field

from ..base import Date, DateTime, Text
from .intangible import Intangible

Date_DateTime = Union[Date, DateTime]

class Role(Intangible):
    """Represents additional information about a relationship or property. For example a Role can be used to say that a 'member' role linking some SportsTeam to a player occurred during a particular time period. Or that a Person's 'actor' role in a Movie was for some particular characterName. Such properties can be attached to a Role entity, which is then associated with the main entities using ordinary properties like 'member' or 'actor'."""
    schema_type: ClassVar[str] = "Role"
    end_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="endDate", serialization_alias="endDate")
    role_name: Text | list[Text] | None = Field(default=None, validation_alias="roleName", serialization_alias="roleName")
    start_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="startDate", serialization_alias="startDate")
