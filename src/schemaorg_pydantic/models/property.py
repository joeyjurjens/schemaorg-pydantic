from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .intangible import Intangible

if TYPE_CHECKING:
    from .class_ import Class
    from .enumeration import Enumeration

if TYPE_CHECKING:
    Class_Enumeration_Property_Ref = Union[Class, Enumeration, "Property", Ref]
else:
    Class_Enumeration_Property_Ref = Union[Is["Class"], Is["Enumeration"], Is["Property"], Ref]

if TYPE_CHECKING:
    Class_Ref = Union[Class, Ref]
else:
    Class_Ref = Union[Is["Class"], Ref]

if TYPE_CHECKING:
    Property_Ref = Union["Property", Ref]
else:
    Property_Ref = Union[Is["Property"], Ref]


class Property(Intangible):
    """A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property."""
    schema_type: ClassVar[str] = "Property"
    domain_includes: Class_Ref | list[Class_Ref] | None = Field(default=None, validation_alias="domainIncludes", serialization_alias="domainIncludes")
    inverse_of: Property_Ref | list[Property_Ref] | None = Field(default=None, validation_alias="inverseOf", serialization_alias="inverseOf")
    range_includes: Class_Ref | list[Class_Ref] | None = Field(default=None, validation_alias="rangeIncludes", serialization_alias="rangeIncludes")
    superseded_by: Class_Enumeration_Property_Ref | list[Class_Enumeration_Property_Ref] | None = Field(default=None, validation_alias="supersededBy", serialization_alias="supersededBy")
