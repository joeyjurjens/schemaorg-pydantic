from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Node, Ref, Text, Url

if TYPE_CHECKING:
    from .action import Action
    from .creative_work import CreativeWork
    from .event import Event
    from .image_object import ImageObject
    from .organization import Organization
    from .person import Person
    from .property_value import PropertyValue
    from .text_object import TextObject

if TYPE_CHECKING:
    Action_Ref = Union[Action, Ref]
else:
    Action_Ref = Union[Is["Action"], Ref]

if TYPE_CHECKING:
    CreativeWork_Event_Ref = Union[CreativeWork, Event, Ref]
else:
    CreativeWork_Event_Ref = Union[Is["CreativeWork"], Is["Event"], Ref]

if TYPE_CHECKING:
    CreativeWork_Url_Ref = Union[CreativeWork, Url, Ref]
else:
    CreativeWork_Url_Ref = Union[Is["CreativeWork"], Url, Ref]

if TYPE_CHECKING:
    ImageObject_Url_Ref = Union[ImageObject, Url, Ref]
else:
    ImageObject_Url_Ref = Union[Is["ImageObject"], Url, Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    PropertyValue_Text_Ref = Union[PropertyValue, Text, Ref]
else:
    PropertyValue_Text_Ref = Union[Is["PropertyValue"], Text, Ref]

if TYPE_CHECKING:
    TextObject_Text_Ref = Union[TextObject, Text, Ref]
else:
    TextObject_Text_Ref = Union[Is["TextObject"], Text, Ref]


class Thing(Node):
    """The most generic type of item."""
    schema_type: ClassVar[str] = "Thing"
    additional_type: Text | list[Text] | None = Field(default=None, validation_alias="additionalType", serialization_alias="additionalType")
    alternate_name: Text | list[Text] | None = Field(default=None, validation_alias="alternateName", serialization_alias="alternateName")
    description: TextObject_Text_Ref | list[TextObject_Text_Ref] | None = Field(default=None)
    disambiguating_description: Text | list[Text] | None = Field(default=None, validation_alias="disambiguatingDescription", serialization_alias="disambiguatingDescription")
    identifier: PropertyValue_Text_Ref | list[PropertyValue_Text_Ref] | None = Field(default=None)
    image: ImageObject_Url_Ref | list[ImageObject_Url_Ref] | None = Field(default=None)
    main_entity_of_page: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="mainEntityOfPage", serialization_alias="mainEntityOfPage")
    name: Text | list[Text] | None = Field(default=None)
    owner: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    potential_action: Action_Ref | list[Action_Ref] | None = Field(default=None, validation_alias="potentialAction", serialization_alias="potentialAction")
    same_as: Url | list[Url] | None = Field(default=None, validation_alias="sameAs", serialization_alias="sameAs")
    subject_of: CreativeWork_Event_Ref | list[CreativeWork_Event_Ref] | None = Field(default=None, validation_alias="subjectOf", serialization_alias="subjectOf")
    url: Url | list[Url] | None = Field(default=None)
