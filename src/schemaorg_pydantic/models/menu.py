from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .menu_item import MenuItem
    from .menu_section import MenuSection

if TYPE_CHECKING:
    MenuItem_Ref = Union[MenuItem, Ref]
else:
    MenuItem_Ref = Union[Is["MenuItem"], Ref]

if TYPE_CHECKING:
    MenuSection_Ref = Union[MenuSection, Ref]
else:
    MenuSection_Ref = Union[Is["MenuSection"], Ref]


class Menu(CreativeWork):
    """A structured representation of food or drink items available from a FoodEstablishment."""
    schema_type: ClassVar[str] = "Menu"
    has_menu_item: MenuItem_Ref | list[MenuItem_Ref] | None = Field(default=None, validation_alias="hasMenuItem", serialization_alias="hasMenuItem")
    has_menu_section: MenuSection_Ref | list[MenuSection_Ref] | None = Field(default=None, validation_alias="hasMenuSection", serialization_alias="hasMenuSection")
