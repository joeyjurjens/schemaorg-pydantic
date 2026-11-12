from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .interact_action import InteractAction

if TYPE_CHECKING:
    from .audience import Audience
    from .contact_point import ContactPoint
    from .language import Language
    from .organization import Organization
    from .person import Person
    from .thing import Thing

if TYPE_CHECKING:
    R5c65ac19 = Union[Audience, ContactPoint, Organization, Person, Ref]
else:
    R5c65ac19 = Union[Is["Audience"], Is["ContactPoint"], Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]


class CommunicateAction(InteractAction):
    """The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation."""
    schema_type: ClassVar[str] = "CommunicateAction"
    about: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    in_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="inLanguage", serialization_alias="inLanguage")
    recipient: R5c65ac19 | list[R5c65ac19] | None = Field(default=None)
