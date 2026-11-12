from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text, Url
from .creative_work import CreativeWork
from .list_item import ListItem

if TYPE_CHECKING:
    from .how_to_supply import HowToSupply
    from .how_to_tool import HowToTool
    from .media_object import MediaObject

if TYPE_CHECKING:
    HowToSupply_Text_Ref = Union[HowToSupply, Text, Ref]
else:
    HowToSupply_Text_Ref = Union[Is["HowToSupply"], Text, Ref]

if TYPE_CHECKING:
    HowToTool_Text_Ref = Union[HowToTool, Text, Ref]
else:
    HowToTool_Text_Ref = Union[Is["HowToTool"], Text, Ref]

if TYPE_CHECKING:
    MediaObject_Url_Ref = Union[MediaObject, Url, Ref]
else:
    MediaObject_Url_Ref = Union[Is["MediaObject"], Url, Ref]


class HowToDirection(CreativeWork, ListItem):
    """A direction indicating a single action to do in the instructions for how to achieve a result."""
    schema_type: ClassVar[str] = "HowToDirection"
    after_media: MediaObject_Url_Ref | list[MediaObject_Url_Ref] | None = Field(default=None, validation_alias="afterMedia", serialization_alias="afterMedia")
    before_media: MediaObject_Url_Ref | list[MediaObject_Url_Ref] | None = Field(default=None, validation_alias="beforeMedia", serialization_alias="beforeMedia")
    during_media: MediaObject_Url_Ref | list[MediaObject_Url_Ref] | None = Field(default=None, validation_alias="duringMedia", serialization_alias="duringMedia")
    perform_time: Text | list[Text] | None = Field(default=None, validation_alias="performTime", serialization_alias="performTime")
    prep_time: Text | list[Text] | None = Field(default=None, validation_alias="prepTime", serialization_alias="prepTime")
    supply: HowToSupply_Text_Ref | list[HowToSupply_Text_Ref] | None = Field(default=None)
    tool: HowToTool_Text_Ref | list[HowToTool_Text_Ref] | None = Field(default=None)
    total_time: Text | list[Text] | None = Field(default=None, validation_alias="totalTime", serialization_alias="totalTime")
