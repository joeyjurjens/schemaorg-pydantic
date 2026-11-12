from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .intangible import Intangible

if TYPE_CHECKING:
    from .class_ import Class
    from .property import Property

if TYPE_CHECKING:
    Class_Enumeration_Property_Ref = Union[Class, "Enumeration", Property, Ref]
else:
    Class_Enumeration_Property_Ref = Union[Is["Class"], Is["Enumeration"], Is["Property"], Ref]


class Enumeration(Intangible):
    """Lists or enumerations\u2014for example, a list of cuisines or music genres, etc."""
    schema_type: ClassVar[str] = "Enumeration"
    superseded_by: Class_Enumeration_Property_Ref | list[Class_Enumeration_Property_Ref] | None = Field(default=None, validation_alias="supersededBy", serialization_alias="supersededBy")
